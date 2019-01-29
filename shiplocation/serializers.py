from rest_framework import serializers

from shiplocation.models import ShipName, ShipLocation


class ShipSerializer(serializers.ModelSerializer):
    """Ship Serializer"""
    class Meta:
        model = ShipName
        fields = '__all__'


class ShipLocationSerializer(serializers.ModelSerializer):
    """Ship Location Serializer"""
    class Meta:
        model = ShipLocation
        fields = '__all__'
