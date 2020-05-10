from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('kit', views.kit, name='kit'),
    path('<int:order_id>', views.detail, name='detail'),
    path('', views.IndexView.as_view(), name='detail'),
    # path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:order_id>/add_item/', views.add_item, name='add_item'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:order_id>/remove_item/', views.remove_item, name='remove_item'),
]
