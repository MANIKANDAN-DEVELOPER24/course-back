# core/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.conf import settings
from .models import User, Course, Offer, Purchase

from django.db.models import ImageField

class AbsoluteURLModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        for field in self.Meta.model._meta.get_fields():
            if isinstance(field, ImageField):
                field_name = field.name
                if field_name in data and data[field_name]:
                    if request:
                        data[field_name] = request.build_absolute_uri(data[field_name])
                    else:
                        data[field_name] = f"{settings.BACKEND_BASE_URL}{data[field_name]}"
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


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            data['image'] = instance.image.url  # Always send Cloudinary full URL
        return data

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
