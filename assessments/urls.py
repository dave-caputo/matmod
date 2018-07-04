from django.urls import path, include

from . import views

app_name = 'assess'

urlpatterns = [

    path('create-assessment/',
         views.AssessmentCreateView.as_view(),
         name='create'),
    path('assessment-list/',
         views.AssessmentListView.as_view(),
         name='list'),
    path('detail-assessment-<int:pk>/',
         views.AssessmentDetailView.as_view(),
         name='detail'),
    path('update-assessment-<int:pk>/',
         views.AssessmentUpdateView.as_view(),
         name='update'),
    # path('delete-section-<int:pk>/',
    #      views.SectionDeleteView.as_view(),
    #      name='delete'),
]
