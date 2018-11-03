from django.urls import path

from . import views

app_name = 'assess'

urlpatterns = [
    path('create-assessment/', views.AssessmentCreateView.as_view(), name='create'),
    path('assessment-list/', views.AssessmentListView.as_view(), name='list'),
    path('detail-assessment-<int:pk>/', views.AssessmentDetailView.as_view(), name='detail'),
    path('rename-assessment-<int:pk>/', views.AssessmentRenameView.as_view(), name='rename'),
    # path('update-assessment-<int:pk>/', views.AssessmentUpdateView.as_view(), name='update'),
    path('complete-assessment-<int:pk>/', views.AssessmentCompleteView.as_view(), name='complete'),
    path('delete-assessment-<int:pk>/', views.AssessmentDeleteView.as_view(), name='delete'),
]
