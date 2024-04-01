from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from . models import *
from .forms import movieform,ReviewForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Movieapp:profile_view')
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
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                         email=email,password=password)
                send_mail('registration successfull', 'your registration was successfull', settings.DEFAULT_FROM_EMAIL, [email])
                return redirect('Movieapp:login')

        else:
            messages.info(request, "Password not matched")
            print('redirecting to login page')
            return redirect('Movieapp:register')

    return render(request, 'register.html')


def index(request):
    catg=Category.objects.all()
    Movie=movie.objects.all()
    context={
         'movie_list':Movie,'cat':catg
    }
    return render(request,'index.html',context)


def indexCateg(request,cid):
    catg=Category.objects.all()
    Movie=movie.objects.filter(category_id=cid)
    context={
         'movie_list':Movie,'cat':catg
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'Movie':Movie})

def add_movie(request):
    catg=Category.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        cat=request.POST.get('categ')

        Movie=movie(name=name,des=des,year=year,img=img,category_id=cat,user_id=request.user.id)
        Movie.save()
        return redirect('/')
    return render(request,'add.html',{"cat":catg})

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




def profileView(request):
    user=User.objects.get(id=request.user.id)
    return render(request, 'viewProfile.html', {'user': user})


def editProfile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']


        user = User.objects.filter(id=request.user.id).update(username=username,first_name=first_name,last_name=last_name)

        return redirect('Movieapp:profile_view')


    return render(request, 'editProfile.html', {'user': user})




def AddCategory(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        name = request.POST['name']


        if Category.objects.filter(name=name).exists():
            messages.success(request, "cetg exist.")
            return redirect('Movieapp:add_category')
        else:
            categ=Category.objects.create(name=name)
            return redirect('Movieapp:index')


    return render(request, 'categadd.html')


def searchResult(request):
    catg = Category.objects.all()
    Movie = movie.objects.all()
    context = {
        'movie_list': Movie, 'cat': catg
    }

    if request.method == "POST":
        name = request.POST['name']

        Movie = movie.objects.filter(name__icontains=name)
        context = {
            'movie_list': Movie, 'cat': catg
        }
        return render(request,'index.html',context)

    return render(request, 'index.html', context)


def addReview(request,mid):
    mov=movie.objects.get(id=mid)
    if request.method=='POST':
        desc=request.POST['review']
        rat=request.POST['rating']

        rev=review.objects.create(movie_id=mid,comments=desc,rating=rat,user_id=request.user.id)
        return redirect('/')

    return render(request,'review.html',{'mov':mov})