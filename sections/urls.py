from django.urls import path, include

from . import views

app_name = 'sections'

urlpatterns = [

    path('create-section/',
         views.SectionCreateView.as_view(),
         name='create'),
    path('section-list/',
         views.SectionListView.as_view(),
         name='list'),
    path('move-section-<int:pk>-<direction>/',
         views.SectionMoveView.as_view(),
         name='move'),
    path('section-<int:pk>/',
         views.SectionDetailView.as_view(),
         name='detail'),
    path('update-section-<int:pk>/',
         views.SectionUpdateView.as_view(),
         name='update'),
    path('delete-section-<int:pk>/',
         views.SectionDeleteView.as_view(),
         name='delete'),
]
