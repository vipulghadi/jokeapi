from rest_framework import serializers
from .models import Jokes

class JokesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jokes
        fields="__all__"
    
    def create(self, validated_data):
        return Jokes.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance