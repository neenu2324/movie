from django.urls import path
from . import views
app_name='Movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('viewprofile/',views.profileView,name='profile_view'),
    path('editprofile',views.editProfile,name='editprofile'),
    path('addcategory',views.AddCategory,name='add_category'),
    path('categoryList/<cid>',views.indexCateg,name='category_index'),
    path('searchResult', views.searchResult, name='searchResult'),
    path('addreview/<mid>',views.addReview,name='addreview')







]