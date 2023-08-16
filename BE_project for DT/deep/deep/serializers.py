# DTapp/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User  # Add this import
from DT.models import DTmodel

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = DTmodel
        fields = '__all__'

    def create(self, validated_data):
        attendees_data = validated_data.pop('attendees', [])
        event = DTmodel.objects.create(**validated_data)
        event.attendees.set(attendees_data)
        return event

    def update(self, instance, validated_data):
        attendees_data = validated_data.pop('attendees', [])
        instance = super().update(instance, validated_data)
        instance.attendees.set(attendees_data)
        return instance
