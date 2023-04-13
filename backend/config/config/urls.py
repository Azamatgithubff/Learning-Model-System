from django.contrib import admin
from django.urls import path
from courses.views import CourseAPIList, CourseAPIUpdate, CourseAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/course/', CourseAPIList.as_view()),
    path('api/v1/course/<int:pk>/', CourseAPIList.as_view()),
    path('api/v1/<int:pk>/', CourseAPIDestroy.as_view()),
]
