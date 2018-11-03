from django.urls import path

from . import views

app_name = 'qres'
urlpatterns = [
    path('create/', views.QreCreateView.as_view(), name='create'),
    path('list/', views.QreListView.as_view(), name='list'),
    path('detail-questionnaire-<int:pk>/', views.QreDetailView.as_view(), name='detail'),
    path('rename-questionnaire-<int:pk>/', views.QreRenameView.as_view(), name='rename'),
    path('delete-questionnaire-<int:pk>/', views.QreDeleteView.as_view(), name='delete'),
]
