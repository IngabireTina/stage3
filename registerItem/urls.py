from django.urls import path
from . import views

urlpatterns = [

    path('recorditem/', views.recordItem, name='recorditem'),
    path('all_item/', views.allItem, name='all_item'),

    path('updateitem/<str:pk>/', views.updateItem, name='updateitem'),
    path('deleteitem/<str:pk>/', views.deleteItem, name='deleteitem'),

    path('recordstock/', views.recordStock, name='recordstock'),
    path('updatestock/<str:pk>/', views.updateStock, name='updatestock'),
    path('deletestock/<str:pk>/', views.deleteStock, name='deletestock'),
    path('allstock/', views.allStock, name='allstock'),

]
