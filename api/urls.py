from django.urls import path, include
from .views import RegisterUserAPIView, BookViewSet, MarkAsReadAPI
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
  path("mark-as-read",MarkAsReadAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('login/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('',include(router.urls))
]