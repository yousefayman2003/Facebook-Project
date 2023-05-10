from django.shortcuts import render, redirect
from .forms import RegisterForm, PostingModelForm, UserUpdateForm, PostingUpdateForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from .models import User, PostModel, Comment
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})


@login_required
def home(request):
    users = User.objects.raw('SELECT * FROM user')
    posts = PostModel.objects.raw(
        'SELECT * FROM post order by date_created desc')
    if request.method == 'POST':
        form = PostingModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            current_user = request.user
            title = request.POST.get('title')
            content = request.POST.get('content')
            post = PostModel(created_by=current_user,
                             title=title, content=content)
            post.save()
            return redirect('/home')

    else:
        form = PostingModelForm()

    context = {
        'users': users,
        'posts': posts,
        'form': form,
    }

    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'main/home.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        user_form = UserUpdateForm(
            request.POST, instance=request.user)
        if user_form.is_valid():
            instance = user_form.save()
            try:
                uploaded_file = request.FILES['image']
                if uploaded_file:
                    instance.image = uploaded_file
                    instance.save()
            except:
                pass

            redirect('/profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form': user_form,
    }

    return render(request, 'main/profile.html', context)


@login_required
def post_detail(request, pk):
    post = PostModel.objects.raw(f'SELECT * FROM post WHERE id={pk};')[0]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect(f'/post_detail/{pk}')
    else:
        form = CommentForm()
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'main/post_detail.html', context)


@login_required
def post_edit(request, pk):
    post = PostModel.objects.raw(f'SELECT * FROM post WHERE id={pk};')[0]
    if request.method == 'POST':
        form = PostingUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/post_detail/{post.id}')
    else:
        form = PostingUpdateForm(instance=post)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'main/post_edit.html', context)


@login_required
def post_delete(request, pk):
    post = PostModel.objects.raw(f'SELECT * FROM post WHERE id={pk};')[0]
    if request.method == 'POST':
        post.delete()
        return redirect('/home')
    context = {
        'post': post
    }
    return render(request, 'main/post_delete.html', context)
