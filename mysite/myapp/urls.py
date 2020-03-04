from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<str:id>',views.delete),
    path('search/<str:name>',views.search),
    path('add',views.add_product)
]