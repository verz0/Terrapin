from rest_framework import serializers
from .models import IPGeolocation, SecurityInfo, Connection, TimeZone

class SecurityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityInfo
        fields = '__all__'

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fields = '__all__'

class IPGeolocationSerializer(serializers.ModelSerializer):
    security_info = SecurityInfoSerializer()
    connection = ConnectionSerializer()
    timezone = TimeZoneSerializer()

    class Meta:
        model = IPGeolocation
        fields = '__all__'