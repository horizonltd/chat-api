from rest_framework import generics
from . import models
from . import serializers

class LectureList(generics.ListCreateAPIView):
    queryset  = models.Lecture.objects.all()
    serializer_class = serializers.LectureSerializer

class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lecture.objects.all()
    serializer_class = serializers.LectureSerializer