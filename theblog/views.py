from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, UpdateForm
from .models import Post


# def home(request):
# return render(request, 'home.html')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']


class ArticalDetailView(DetailView):
    model = Post
    template_name = 'arical_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_host.html'

    # this is for model form
    # fields = '__all__'
    # fields = ('title', 'body', 'author')


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')