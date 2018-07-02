from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('client-detail-<int:pk>', views.ClientDetailView.as_view(),
         name='detail'),
]
