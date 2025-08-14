# core/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.conf import settings
from .models import User, Course, Offer, Purchase

# Automatically convert ALL ImageFields to absolute URLs
class AbsoluteURLModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        for field_name, field_value in data.items():
            model_field = self.Meta.model._meta.get_field(field_name) if field_name in self.Meta.model._meta.fields_map else None
            if model_field and model_field.get_internal_type() == "ImageField" and field_value:
                if request:
                    data[field_name] = request.build_absolute_uri(field_value)
                else:
                    data[field_name] = f"{settings.BACKEND_BASE_URL}{field_value}"
        return data


class UserSerializer(AbsoluteURLModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user


class CourseSerializer(AbsoluteURLModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class OfferSerializer(AbsoluteURLModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'course', 'purchased_at']
