from django.urls import path
# from . import views
from .views import *

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'), 
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
#     path('drafts/', views.post_draft_list, name='post_draft_list'),
# ]

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<pk>/publish/',post_publish, name='post_publish'),
    path('post/<pk>/remove/',post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('drafts/',post_draft_list, name='post_draft_list'),
    path('post/new/',post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('contact/', contact, name='contact'),


]