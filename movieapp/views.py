from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from .forms import ReviewForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login

from .forms import ReviewForm 



from django.views.generic.edit import UpdateView, DeleteView
from .models import Movie
from .models import Review

class CustomLoginView(LoginView):
    template_name = 'movie/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('review_list')
    
class RegisterPage(FormView):
    template_name = 'movie/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('review_list')
        return super(RegisterPage, self).get(*args, **kwargs)


class MovieList(ListView):
    model = Movie
    template_name='movie/movie_list.html'
    context_object_name = 'movies'

class MovieDetail(DetailView):
    model = Movie
    template_name='movie/movie.html'
    context_object_name = 'movie'

class ReviewList(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'movie/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['reviews'] = context['reviews'].filter(
                movie__title__contains=search_input)
            
        context['search_input'] = search_input

        return context

      

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movie/review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movie/edit_review.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')
    

class ReviewDetail(LoginRequiredMixin, DetailView):
    model = Review
    template_name = 'movie/review.html'
    context_object_name = 'review'

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'movie/delete_review.html'  # Specify your delete template
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')



