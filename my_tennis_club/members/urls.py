from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('members.urls')),  # This makes / go to your members app
    path('admin/', admin.site.urls),
]