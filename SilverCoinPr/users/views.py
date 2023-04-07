from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DateDetailView, CreateView, DetailView
from django.shortcuts import render, redirect
from django.contrib import auth
from registers.views import menu, menu_invisible
from .models import *
from .forms import *

# def SuccessLoginView(request):
#     context = {'menu': menu,
#                'menu_invisible': menu_invisible,
#                'title': 'Success!'
#                }
#     return render(request, 'users/success_login.html', context=context)
#
#
# def LoginView(request):
#     context = {'menu': menu,
#                'menu_invisible': menu_invisible,
#                "form": RegisterUserForm(),
#                'title': 'Create an account'
#                }
#     return render(request, 'users/login.html', context=context)
#
#
# def SigninView(request):
#     context = {'menu': menu,
#                'menu_invisible': menu_invisible,
#                'title': 'Sign in'
#                }
#     return render(request, 'users/signin.html', context=context)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users/success_login.html')

    def get_context_data(self, *, object_list, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Create an account')
        return dict(list(context.items()) + list(c_def.items()))


# class LoginUser('LoginView'):
#     form_class = AuthenticationForm
#     template_name = 'registers/signin.html'

    # def get_context_data(self, *, object_list, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Sign in')
    #     return dict(list(context.items()) + list(c_def.items()))