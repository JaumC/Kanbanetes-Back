from django.contrib import admin
from django.urls import path, include
from backend.views import signup, signin, profile
from rest_framework.routers import DefaultRouter
from backend.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
