from django.urls import path

from . import views

app_name = 'clients'
urlpatterns = [
    path('create/',
         views.ClientCreateView.as_view(),
         name='create'),
    path('list/',
         views.ClientListView.as_view(),
         name='list'),
    path('detail-client-<int:pk>', views.ClientDetailView.as_view(),
         name='detail'),
    path('update-client-<int:pk>/',
         views.ClientUpdateView.as_view(),
         name='update'),
]
