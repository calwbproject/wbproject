from rest_framework import serializers
from django.contrib.auth.models import User

from whiteboard.models import Company, Engineer
from whiteboard.serializers import CompanySerializer, EngineerSerializer


class UserSimpleSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    companies = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'companies')
    
    def get_companies(self, obj):
        
        company_ids = Engineer.objects.filter(sales_name=obj).values_list('company_name',flat=True).distinct()
        companies = Company.objects.filter(id__in=company_ids)
        
        return None
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    