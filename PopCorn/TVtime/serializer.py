from rest_framework import serializers
from .models import Movies,UserProfile
from django.contrib.auth.models import User


class Movieserializer(serializers.Serializer):
    name=serializers.CharField()
    year=serializers.IntegerField()
    Director=serializers.CharField()
    Genre=serializers.CharField()

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    bgimg = serializers.CharField()
    poster = serializers.CharField()
    rate = serializers.FloatField()


class MovieModelSer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=["username","password","email","password2"]

    def create(self, validated_data):
        password2 = validated_data.pop('password2', None)
        if validated_data['password'] != password2:
            raise serializers.ValidationError("Passwords do not match")
        
        user = User.objects.create_user(**validated_data)
        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'profile_pic', 'dob', 'gender', 'phone']



    
# class UserRevSer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=["first_name","last_name","username"]

# class MovieSer(serializers.ModelSerializer):
#     class Meta:
#         model=Movies
#         fields=["name","year"]

   

# class ReviewSerializer(serializers.ModelSerializer):
#     movie=MovieSer(read_only=True)
#     user=UserRevSer(read_only=True)
#     class Meta:
#         model=Review
#         fields=["review","rating","date","movie","user"]
    
#     def create(self, validated_data):
#         user=self.context.get("user")
#         mv=self.context.get("movie")
#         return Review.objects.create(**validated_data,user=user,movie=mv)