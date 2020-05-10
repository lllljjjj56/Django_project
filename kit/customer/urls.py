from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kit', views.kit, name='kit'),
    path('<int:customer_id>', views.detail, name='detail'),
    path('query', views.query, name='query')
]
