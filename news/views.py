from django.shortcuts import render
from .models import Core
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    model = Core
    template_name = 'index.html'
    context_object_name = 'index'
    
class SingleView(DetailView):
    model = Core
    template_name = 'single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = Core
    template_name = 'posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Core
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('news:posts')

class EditView(UpdateView):
    model = Core
    template_name = 'edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('news:posts')

class Delete(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('news:posts')
    template_name = 'delete.html'
