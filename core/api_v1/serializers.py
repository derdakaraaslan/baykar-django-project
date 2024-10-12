from rest_framework import serializers
from core.models.users import User
from core.models.parts import Part
from core.models.aircrafts import Aircraft
from core.models.teams import Team

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'name', 'aircraft', 'team', 'stock']

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']
