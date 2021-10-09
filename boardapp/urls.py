from django.urls import path

from boardapp.views import board_list


urlpatterns = [
    #board/
    path('', board_list, name='board_list')
]