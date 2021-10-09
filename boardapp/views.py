from django.shortcuts import render
from boardapp.models import text
# Create your views here.

def board_list(request):
    text_objects = text.objects.all()
    context = {
        'posts': text_objects
    }
    return render(request, 'board_list.html', context=context)