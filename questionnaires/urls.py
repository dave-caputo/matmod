from django.urls import path

from . import views

app_name = 'qres'
urlpatterns = [

    # Questionnaires...
    path('create/', views.QreCreateView.as_view(), name='create'),
    path('list/', views.QreListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.QreDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.QreUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.QreDeleteView.as_view(), name='delete'),

    # Sections...
    path('questionnaire-<int:qre_id>/create-section/',
         views.SectionCreateView.as_view(),
         name='section_create'),
    path('questionnaire-<int:qre_id>/section-list/',
         views.SectionListView.as_view(),
         name='section_list'),

]
