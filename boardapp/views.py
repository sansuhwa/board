from django.shortcuts import render, redirect
from boardapp.models import text, Post
from django.http.response import HttpResponse
# Create your views here.

def board_list(request):
    post_objects = Post.objects.all()
    context = {
        'posts': post_objects
    }
    return render(request, 'board_list.html', context=context)

def detail_post(requset, post_id):
    detail_post=Post.objects.get(id=post_id)
    context = {
        'post': detail_post
    }
    return render(requset, 'detail_post.html', context=context)
    

def create_post(request):
    if request.method == 'GET':
        return render(request, 'create_post.html')
    if request.method == 'POST':
        text_model = request.POST
        text_model_title = text_model['title']
        text_model_description = text_model['description']
        post = Post.objects.create(title=f'{text_model_title}', description=f'{text_model_description}')
        context = {
           'post': post
        }
        return render(request, 'detail_post.html', context=context)

def update_post(requset, post_id):
    if requset.method == 'GET':
        post = Post.objects.get(id=post_id)
        context = {
            'post': post
        }
        return render(requset, 'update_post.html', context=context)
    if requset.method == 'POST':
        post_model: dict = requset.POST
        post_model_title = post_model['title']
        post_model_description = post_model['description']
        post = Post.objects.get(id=post_id)
        post.title = post_model_title
        post.description = post_model_description
        post.save()
        context = {
            'post': post
        }
        return render(requset, 'detail_post.html', context=context)


def delete_post(req, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    post.save()
    response = redirect('/board/')
    return response
    