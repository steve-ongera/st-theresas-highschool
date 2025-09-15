from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from website.views import custom_page_not_found, custom_server_error

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
]

# Static & media serving (only in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Error handlers
handler404 = custom_page_not_found
handler500 = custom_server_error
