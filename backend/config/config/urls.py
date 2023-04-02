from django.contrib import admin
from django.urls import path, include, re_path

from courses.views import CourseAPIList, CourseAPIUpdate, CourseAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/course/', CourseAPIList.as_view()),
    path('api/v1/course/<int:pk>/', CourseAPIUpdate.as_view()),
    path('api/v1/coursedelete/<int:pk>/', CourseAPIDestroy.as_view()),

]
