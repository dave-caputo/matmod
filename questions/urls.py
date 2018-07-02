from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [

    # Questions...
    path('create-question/',
         views.QuestionCreateView.as_view(),
         name='create'),
    path('question-list/',
         views.QuestionListView.as_view(),
         name='list'),
    path('move-question-<int:pk>-<direction>/',
         views.QuestionMoveView.as_view(),
         name='move'),
    path('question-detail-<int:pk>/',
         views.QuestionDetailView.as_view(),
         name='detail'),

]
