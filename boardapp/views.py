from django.shortcuts import render

# Create your views here.

def board_html(request):
    context = {

    }
    return render(request, 'board.html', context=context)