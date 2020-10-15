from rest_framework import serializers
from .models import User, Account, Plotter, Pattern
from rest_framework.authtoken.models import Token
from django.db import transaction


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="accounts:users-detail", read_only=True)

    class Meta:
        model = Account
        fields = ('url', 'id', 'username', 'email', 'password',
                  'last_used_time', 'total_usages', 'daily_usage',
                  'usages_for_last_week',
                  'is_superuser', 'is_staff', 'is_admin', 'is_dealer')
        extra_kwargs = {'password': {'write_only': True},
                        'is_superuser': {'read_only': True},
                        'is_staff': {'read_only': True},
                        'is_dealer': {'read_only': True},
                        'is_admin': {'read_only': True}
                        }

    @transaction.atomic
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = ('username', 'password',)


class PlottersSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="accounts:plotters-detail", read_only=True)
    # use_url = serializers.HyperlinkedIdentityField(
    #     view_name="accounts:plotter-use", read_only=True)
    patterns = serializers.HyperlinkedIdentityField(
        view_name="accounts:patterns-list", read_only=True)

    class Meta:
        model = Plotter
        fields = ('url', 'id', 'dealers_email', 'model', 'description',
                  'last_used_time', 'total_usages', 'daily_usage',
                  'usages_for_last_week', 'patterns',)


class UsePlotterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plotter
        fields = ()


class PatternsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="accounts:patterns-detail", read_only=True)

    class Meta:
        model = Pattern
        fields = ('url', 'id', 'name', 'description',
                  'last_used_time', 'total_usages', 'daily_usage',
                  'usages_for_last_week',)
