from rest_framework import serializers
from db.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "phone",
            "height",
            "weight",
            "avatar",
        ]