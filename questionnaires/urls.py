from django.urls import path

from . import views

app_name = 'qres'
urlpatterns = [
    path('create/', views.QreCreateView.as_view(), name='create'),
    path('list/', views.QreListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.QreDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.QreUpdateView.as_view(), name='update')
]
