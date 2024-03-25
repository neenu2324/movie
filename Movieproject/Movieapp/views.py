from django.contrib.auth.hashers import make_password
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from . models import movie
from .forms import movieform,ReviewForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Movieapp:index')
        else:
            messages.info(request, "Invalid")
            return redirect('Movieapp:login')
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['password1']

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already in use")
                return redirect('Movieapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already in use")
                return redirect('Movieapp:register')
            else:
                hashed_password = make_password(password)
                User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                         email=email, password=hashed_password)
                messages.success(request, "Welcome,Your registration was successful.")
                return redirect('Movieapp:login')
        else:
            messages.info(request, "Password not matched")
            return redirect('Movieapp:register')

    return render(request, 'register.html')


def index(request):
    Movie=movie.objects.all()
    context={
         'movie_list':Movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'Movie':Movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        Movie=movie(name=name,des=des,year=year,img=img)
        Movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'Movie':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
def review(request,id):
    Movie = movie.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = Movie
            review.save()
            return redirect('Movieapp:detail', movie_id=id)
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'Movie': Movie})