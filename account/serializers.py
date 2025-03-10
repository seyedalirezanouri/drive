from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import User


class RegistrationSerializer(ModelSerializer):
    password = CharField(write_only=True)
    repeat_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repeat_password')
    
    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise ValidationError("Passwords must match!")
        validate_password(data['password'])
        return data
