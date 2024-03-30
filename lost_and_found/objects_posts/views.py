from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from lost_and_found import settings
from lost_and_found.objects_posts.models import Post
from lost_and_found.objects_posts.forms import PostCreateForm, ObjectForm, PostEditForm, LoginForm, CreateUserForm
from lost_and_found.utils.mixins import InputStyleMixin
# from lost_and_found.objects_posts.tasks import send_register_email


def index(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'index.html', context)


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'post_form': form}
    return render(request, 'post_edit.html', context)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')


def found(request, pk):
    post = Post.objects.get(pk=pk)
    post.found = True
    post.save()
    return redirect('index')


def create(request):
    post_form = PostCreateForm()
    object_form = ObjectForm()
    if request.method == "POST":
        post_form = PostCreateForm(request.POST)
        object_form = ObjectForm(request.POST)

        if post_form.is_valid() and object_form.is_valid():
            obj = object_form.save()
            post = post_form.save(commit=False)
            post.object = obj
            post.save()

            return redirect('index')

    context = {
        'post_form': post_form,
        'object_form': object_form,
    }

    return render(request, 'post_create.html', context)

class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "login-main.html"


def send_register_email(request):
    subject = 'Login Notification',
    message = 'You have logged in successfully.',
    email_from = settings.EMAIL_HOST_USER,
    recipient_list = [User.objects.all().last().email],
    send_mail( subject, message, email_from, recipient_list )


class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_register_email(self.request)
        return response



def user_logout(request):
    logout(request)
    return redirect('index')
