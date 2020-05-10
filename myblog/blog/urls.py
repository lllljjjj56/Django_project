from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'article/<int:article_id>/', views.article_page, name='article_page'),
    path(r'edit/<int:article_id>/', views.edit_page, name='edit_page'),
    path(r'edit/action/', views.edit_action, name='edit_action'),
]
