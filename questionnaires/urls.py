from django.urls import path

from .views import QreCreateView, QreListView

app_name = 'qres'
urlpatterns = [
    path('create/', QreCreateView.as_view(), name='create'),
    path('list/', QreListView.as_view(), name='list'),
]
