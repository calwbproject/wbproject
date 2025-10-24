from rest_framework import serializers
from django.contrib.auth.models import User

from whiteboard.models import Company, Engineer
from whiteboard.serializers import CompanySerializer, EngineerSerializer, EngineerSimpleSerializer


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
    engineers_length = serializers.SerializerMethodField()
    engineer_group_by_type = serializers.SerializerMethodField()
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'engineer_group_by_type' ,'first_name', 'last_name', 'password', 'engineers_length', 'companies')
    
    def get_companies(self, obj):
        
        company_ids = Engineer.objects.filter(sales_name=obj).values_list('company_name',flat=True).distinct()
        companies = Company.objects.filter(id__in=company_ids)
        
        result = []
        for company in companies:
            engineers = Engineer.objects.filter(company_name = company, sales_name = obj)
            if engineers.exists():
                company_data = CompanySerializer(company).data
                company_data['engineers'] = EngineerSerializer(engineers, many=True).data
                result.append(company_data)
            
        return result
        # return CompanySerializer(companies, many=True).data
    
    def get_engineers_length(self, obj):
        
        return Engineer.objects.filter(sales_name=obj).count()
    
    def get_engineer_group_by_type(self, obj):
        result = {}
        for i in range(5):
            engineers = Engineer.objects.filter(sales_name=obj, engineer_status=i)
            result[i] = EngineerSimpleSerializer(engineers, many=True).data
        return result
        
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    