from rest_framework import serializers
from db.models import Workouts

# Django API используя Django Rest Framework

class WorkoutSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name_workout = serializers.CharField(max_length=50)
    date_create = serializers.DateTimeField(read_only=True)
    exercise_name = serializers.CharField(max_length=50)
    number_of_approaches = serializers.IntegerField()
    amount_of_exercise = serializers.IntegerField()
    distance = serializers.DecimalField(max_digits=5, decimal_places=2)
    workout_time = serializers.DecimalField(max_digits=5, decimal_places=2)
    photo_workout = serializers.ImageField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Workouts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.name_workout = validated_data.get('name_workout', instance.name_workout)
        instance.exercise_name = validated_data.get('exercise_name', instance.exercise_name)
        instance.number_of_approaches = validated_data.get('number_of_approaches', instance.number_of_approaches)
        instance.amount_of_exercise = validated_data.get('amount_of_exercise', instance.amount_of_exercise)
        instance.distance = validated_data.get('distance', instance.distance)
        instance.workout_time = validated_data.get('workout_time', instance.workout_time)
        instance.photo_workout = validated_data.get('photo_workout', instance.photo_workout)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance



