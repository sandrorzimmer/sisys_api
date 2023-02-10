from django.urls import path, include

from rest_framework.routers import DefaultRouter

from sisys_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('tag', views.TagViewSet)
router.register('info', views.InfoViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]