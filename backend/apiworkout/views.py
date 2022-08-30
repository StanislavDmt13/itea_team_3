from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializer import WorkoutSerializer
from db.models import Workouts


# Viewsets Django REST Framework
class WorkoutViewSet(viewsets.ModelViewSet):

    serializer_class = WorkoutSerializer
    queryset = Workouts.objects.all()

    def list(self, request):
        queryset = Workouts.objects.filter(user=request.user).order_by('-date_create')
        serializer = WorkoutSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Workouts.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = WorkoutSerializer(user)
        return Response(serializer.data)




"""
# Django API используя Django Rest Framework

class WorkoutAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (AllowAny,)

    def get(self, request):
        workouts = Workouts.objects.filter(user=request.user).order_by('-date_create')
        serializer = WorkoutSerializer(workouts, many=True)
        return Response({"workouts": serializer.data})

    def post(self, request):
        workout = request.data
        serializer = WorkoutSerializer(data=workout)

        if serializer.is_valid(raise_exception=True):
            workout_saved = serializer.save()

        return Response({"workout": "Workout '{}' created successfully".format(workout_saved.name_workout)})

    def put(self, request, pk):
        saved_workout = get_object_or_404(Workouts.objects.all(), pk=pk)
        data = request.data
        serializer = WorkoutSerializer(instance=saved_workout, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            workout_saved = serializer.save()

        return Response({
            "success": "Workout '{}' updated successfully".format(workout_saved.name_workout)
        })

    def delete(self, request, pk):
        workout = get_object_or_404(Workouts.objects.all(), pk=pk)
        workout.delete()
        return Response({
            "message": "Workout with id `{}` has been deleted.".format(pk)
        }, status=204)
        
"""