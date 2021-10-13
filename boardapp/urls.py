from django.urls import path

from boardapp.views import board_list

from boardapp.views import create_post

from boardapp.views import detail_post

urlpatterns = [
    #board/
    path('', board_list, name='board_list'),
    path('create/', create_post, name='creat_post'),
    #board/<post_id>
    path('<int:post_id>/', detail_post, name='detail.post')
]