from django.contrib import admin 
from django.urls import path, include
from karaoke import urls

urlpatterns= [
    path('admin/', admin.site.urls),
    path('', include(karaoke.urls)),
]