from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader 
from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

# vistas genericas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView,
    DeleteView
)

from .forms import ProductForm
from .models import Product

from .mixins import LoginRequiredMixin 

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductNew(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('products:hello')
    fields = ['name', 'description', 'category', 'price', 'image']

class ProductEdit(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('products:hello')
    fields = ['name', 'description', 'category', 'price', 'image']

class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:hello')

def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username, 
                                            password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('/')

    context = {}
    return render(request, 'login/login.html')