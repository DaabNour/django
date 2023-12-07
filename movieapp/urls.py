from django import views
from django.urls import path
from .views import CustomLoginView, MovieDetail, MovieList, RegisterPage, ReviewCreate, ReviewDeleteView, ReviewDetail, ReviewList, ReviewUpdate, LogoutView
from movieapp import admin

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('movies/', MovieList.as_view(), name='movie_list'),
    path('reviews/', ReviewList.as_view(), name='review_list'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie'),
    path('addreview/', ReviewCreate.as_view(), name='addreview'), 
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review'),
    path('reviewupdate/<int:pk>/', ReviewUpdate.as_view(), name='reviewupdate'), 
    path('reviewdelete/<int:pk>/', ReviewDeleteView.as_view(), name='reviewdelete'),

]