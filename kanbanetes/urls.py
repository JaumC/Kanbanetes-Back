from django.contrib import admin
from django.urls import path, include
from backend.views import signup, signin
from rest_framework.routers import DefaultRouter
from backend.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
