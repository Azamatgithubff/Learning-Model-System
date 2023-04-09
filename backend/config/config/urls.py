from django.contrib import admin
from django.urls import path, include, re_path

from courses.views import CourseAPIList, CourseAPIUpdate, CourseAPIDestroy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/course/', CourseAPIList.as_view()),
    path('api/v1/course/<int:pk>/', CourseAPIUpdate.as_view()),
    path('api/v1/coursedelete/<int:pk>/', CourseAPIDestroy.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
