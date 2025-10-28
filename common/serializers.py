from rest_framework import serializers
from django.contrib.auth.models import User

from whiteboard.models import Company, Engineer
from whiteboard.serializers import CompanySerializer, CompanySimpleSerializer, EngineerSerializer, EngineerSimpleSerializer


# transfer only user table data
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
    

#conclude
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    companies = serializers.SerializerMethodField()
    # engineers_length = serializers.SerializerMethodField()
    engineer_group_by_status = serializers.SerializerMethodField()
    engineers = serializers.SerializerMethodField()
    
    
    class Meta:
        model = User
        fields = ('username', 'engineers', 'engineer_group_by_status' ,'first_name', 'last_name', 'password', 'companies')
    
    def get_companies(self, obj):
        
        company_ids = Engineer.objects.filter(sales_id=obj).values_list('company_id',flat=True).distinct()
        companies = Company.objects.filter(id__in=company_ids)
        
        result = []
        for company in companies:
            engineers = Engineer.objects.filter(company_id = company, sales_id = obj)
            if engineers.exists():
                company_data = CompanySimpleSerializer(company).data
                company_data['engineers'] = [e['id'] for e in EngineerSimpleSerializer(engineers, many=True).data]
                result.append(company_data)
        return result
        # return CompanySerializer(companies, many=True).data
    
    # def get_engineers_length(self, obj):
        
    #     return Engineer.objects.filter(sales_name=obj).count()
    
    def get_engineer_group_by_status(self, obj):
        result = {}
        status_list = ['勤務中', '今月入社', '来月入社', '今回終了', '他']
        for i in status_list:
            engineers = Engineer.objects.filter(sales_id=obj, engineer_status=i)
            result[i] = [e['id'] for e in EngineerSimpleSerializer(engineers, many=True).data]
        return result
    
    def get_engineers(self, obj):
        
        engineers = Engineer.objects.filter(sales_id=obj)
        return EngineerSimpleSerializer(engineers, many=True).data
        
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    