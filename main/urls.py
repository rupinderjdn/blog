from django.urls import path
from main import views

urlpatterns=[
    path('',views.index,name='index'),
    path('article/<int:pk>',views.article,name='show_article'),
    path('author/<int:pk>',views.author,name='show_author'),
    path('article',views.create_article,name='create_article'),
    path('author',views.create_author,name='create_author')
]
