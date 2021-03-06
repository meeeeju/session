from django.contrib import admin
from django.urls import path,include
from . import views

#연결시켜 주는 곳

urlpatterns = [
    path('', views.blog , name="blog"),
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name='create'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
    path('update/<int:blog_id>', views.update, name='update'),
    #comment

    path('comment/<int:blog_id>',views.comment,name='comment'),
    path('comment/delete/<int:comment_id>',views.comment_delete,name='comment_delete'),
    #like
    path('like/<int:blog_id>',views.post_like,name='post_like'),
]
