from django.contrib import admin
from django.urls import path, include
from users import views as users_views  
from library import views as library_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.index, name='index'),  
    path('users/', include('users.urls')),  
    path('library/', include('library.urls')),  
]