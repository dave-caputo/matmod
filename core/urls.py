"""matmod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path, reverse

urlpatterns = [
    path('', lambda x: HttpResponseRedirect(reverse('dashboard:index'))),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('answers/', include('answers.urls')),
    path('clients/', include('clients.urls')),
    path('assessments/client-<int:client_pk>/', include('assessments.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('questionnaires/', include('questionnaires.urls')),
    path('sections/qre-<int:qre_pk>/', include('sections.urls')),
    path('questions/qre-<int:qre_pk>/section-<int:section_pk>/',
         include('questions.urls'))
]
