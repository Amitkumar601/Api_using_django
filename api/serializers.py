from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    #Creating create method to create data in DB.
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
     
     #Creating update method to update data in DB.
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    #validating data    
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats are Full')
        return value
           

