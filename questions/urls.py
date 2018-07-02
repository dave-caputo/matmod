from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [

    # Questions...
    path('<int:qre_pk>/section-<int:section_pk>/create-question/',
         views.QuestionCreateView.as_view(),
         name='create'),
]
