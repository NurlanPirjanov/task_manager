from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import private_storage.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_my/', include('task.urls')),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('p_media/', include(private_storage.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)