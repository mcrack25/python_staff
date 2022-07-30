from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from album.views import photo_list
from rest_framework.routers import DefaultRouter
from core.api.urls import router as core_router
from departments.api.urls import router as department_router


router = DefaultRouter()
router.registry.extend(core_router.registry)
router.registry.extend(department_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', photo_list, name='photo_list'),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
