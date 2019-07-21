from django.urls import path

from . import views

urlpatterns = [
    # ex: /spares/
    path('', views.index, name='index'),
    path('sheet', views.sheet, name='sheet'),
    path('datatables', views.datatables, name='datatables'),
    path('jump/', views.jump, name='jump'),
    path('addrow/', views.addrow, name='addrow'),
    path('reedit/', views.reedit, name='reedit'),
    path('changed/<int:getid>/', views.changed, name='changed'),
]