from django.urls import path, include

from . import views

app_name = 'qres'
urlpatterns = [

    # Questionnaires...
    path('create/',
         views.QreCreateView.as_view(),
         name='create'),
    path('list/',
         views.QreListView.as_view(),
         name='list'),
    path('detail-questionnaire-<int:pk>/',
         views.QreDetailView.as_view(),
         name='detail'),
    path('update-questionnaire-<int:pk>/',
         views.QreUpdateView.as_view(),
         name='update'),
    path('delete-questionnaire-<int:pk>/',
         views.QreDeleteView.as_view(),
         name='delete'),
]
