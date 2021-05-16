from django.shortcuts import render, redirect, reverse, get_object_or_404
from django import forms
from django.contrib.auth import authenticate
from django.views.generic import ListView
from django.contrib.auth.models import User, auth
from .forms import PostForm, CommentForm, PasswordResetForm
from .models import Post, Author
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):

    posts = Post.objects.order_by('-timestamp')[:]
    # print(get_absolute_url())

    context = {
        "posts": posts
    }
    return render(request, 'home.html', context)




def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    # if request.method == 'POST':
        # if form.is_valid():
        #     form.instance.user = request.user
        #     form.instance.post = post
        #     form.save()
        #     return redirect('')
    

    context = {
        'form': form,
        "post": post
        
    }
    
    return render(request, "post_detail.html", context)    

def create_post(request):
    form = PostForm(request.POST or None)
    

    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
            return redirect(reverse('post_detail', kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
    }



    return render(request, 'post_create.html', context)



def post_edit(request, id):

    post = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("post created")
            return redirect(reverse('post_detail', kwargs={
                'id': form.instance.id
            }))

    
    context = {
        'form': form,
    }



    return render(request, 'post_create.html', context)



def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('home'))



# def reset_password(request):
#     form = PasswordResetForm(request.POST or None)
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         get_user_object = User.objects.all()
#         for i in get_user_object:
#             if username==i.username and email==i.email:
#                 print("they match")
#                 return redirect(reverse('account_set_password'))
#             else:
#                 print("no match")
#         #     print(i.email)
#         #     # print(i)
#         # print(get_user_object)
#             # user = authenticate(username=username, email=email)
            
#                 # print("user not exist")
#                 # raise forms.ValidationError("This user does not exist")
#         # if form.is_valid():
#         #     form.save()
#             # print("post created")
    
#     context = {
#         'form': form
#     }
    
    
#     return render(request, 'account/password_reset.html', context)

# subject = 'Password Reset'
# message = f'Hello, '