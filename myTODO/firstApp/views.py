
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


from .models import TODO


def home(request):
    return render(request, 'home.html')


def user_signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
            return redirect('/user_signup/')

        my_user = User.objects.create_user(username=uname, password=pwd)
        my_user.save()
        return redirect('/user_login/')

    return render(request, 'user_signup.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        new_user = authenticate(request, username=uname, password=pwd)

        if new_user is not None:
            login(request, new_user)
            return redirect('/main_page/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/user_login/')
    return render(request, 'user_login.html')


def main_page(request):
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redirect to login page

    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            obj = TODO(title=title, user=request.user)
            obj.save()
    todos = TODO.objects.filter(user=request.user)
    return render(request, 'main_page.html', {'todos': todos})


def delete(request, d_id):
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redirect to login page

    if request.method == "POST":
        todo = get_object_or_404(TODO, id = d_id, user = request.user)
        todo.delete()
    return redirect('/main_page/')

# def todo_update(request, u_id):
#     if not request.user.is_authenticated:
#         return redirect('user_login')
#     if request.method == "POST":
#         todo = get_object_or_404(TODO, id = u_id, user = request.user)


def todo_update(request, u_id):
    todo = get_object_or_404(TODO, id=u_id, user=request.user)

    if request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')

        if title:
            todo.title = title
        if status:
            todo.status = status

        todo.save()  # Save changes

        return redirect('main_page')

    return render(request, 'todo_update.html', {'todos': todo})  # Show form


def user_logout(request):
    logout(request)
    return redirect('user_login')
