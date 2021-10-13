from django.shortcuts import render
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
        post = text.objects.create(title=f'{text_model_title}', description=f'{text_model_description}')
        context = {
           'post': post
        }
        return render(request, 'detail_post.html',context=context)
        
        
        
