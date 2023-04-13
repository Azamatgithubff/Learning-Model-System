from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Course
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import CourseSerializer


class CourseAPIList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)

class CourseAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CourseAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)



