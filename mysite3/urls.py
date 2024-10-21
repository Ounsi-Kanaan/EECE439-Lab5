from django.contrib import admin
from django.urls import path, include
from myapp3.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # The root URL shows the home view
    path('myapp3/', include('myapp3.urls')),  # Include URLs from myapp3
]
