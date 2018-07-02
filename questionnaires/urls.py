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
    path('<int:qre_id>/create-section/',
         views.SectionCreateView.as_view(),
         name='section_create'),
    path('<int:qre_id>/section-list/',
         views.SectionListView.as_view(),
         name='section_list'),
    path('<int:qre_id>/move-section-<int:pk>-<direction>/',
         views.SectionMoveView.as_view(),
         name='section_move'),
    path('<int:qre_id>/section-<int:pk>/',
         views.SectionDetailView.as_view(),
         name='section_detail'),
    path('<int:qre_id>/update-section-<int:pk>/',
         views.SectionUpdateView.as_view(),
         name='section_update'),
    path('<int:qre_id>/delete-section-<int:pk>/',
         views.SectionDeleteView.as_view(),
         name='section_delete'),
]
