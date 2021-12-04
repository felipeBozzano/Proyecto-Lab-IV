from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

title = 'MyUbp'

urlpatterns = [
    path('api/v1/doc', include_docs_urls(title=title)),
    path('api/', include('users.urls')),
    path('api/', include('degrees.urls')),
    path('api/', include('users_degrees.urls')),
    path('api/', include('subjects.urls')),
    path('api/', include('notes.urls')),
    path('api/', include('correlatives.urls')),
    path('admin/', admin.site.urls),
]
