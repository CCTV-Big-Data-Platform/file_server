import os
from .models import File
from rest_framework import serializers


class FileUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields='__all__'
        # read_only_fields = '__all__'
    def validate(self, validated_data):
        validated_data['name'] = os.path.splitext(validated_data['file'].name)[0]
        return validated_data
    def create(self,validated_data):
        return File.objects.create()