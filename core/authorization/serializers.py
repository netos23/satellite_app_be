from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from . import models
from . import validators
from .models import Users


class RequestUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    second_name = serializers.CharField(required=False, source='last_name')
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=False, validators=(validators.validate_phone,))
    gender = serializers.ChoiceField(choices=models.Users.GENDERS, required=False)
    birthday = serializers.DateField(required=False, input_formats=["%d.%m.%Y", "%Y-%m-%d"])
    role = serializers.ChoiceField(choices=models.Users.ROLES, required=False)


class RequestFarmerSerializer(serializers.Serializer):
    brand = serializers.CharField()
    address = serializers.CharField()


class JWTRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    access_token = serializers.CharField(read_only=True)
    token_class = RefreshToken

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh_token"])

        data = {"access_token": str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh_token"] = str(refresh)
            user_id = refresh.access_token.get("user_id")
            Users.objects.filter(id=user_id).update(refresh_token=str(refresh))
        return data


class ResponseUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    second_name = serializers.CharField(required=False, source='last_name')
    gender = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    brand = serializers.CharField(required=False)
    address = serializers.CharField(required=False)


    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_role(self, obj):
        return obj.get_role_display()

    class Meta:
        model = Users
        exclude = (
            "id",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "is_verified",
            "username",
            "name",
            "last_login",
            "groups",
            "user_permissions",
            "last_name",
            "refresh_token",
        )


class AuthResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
