from django.conf.urls.static import static
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
