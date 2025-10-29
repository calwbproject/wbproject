from django.contrib.auth.models import User
from rest_framework import serializers

from whiteboard.models import Company, Engineer

class CompanySerializer(serializers.ModelSerializer):
    
    engineers = serializers.SerializerMethodField()
    
    class Meta:
        model= Company
        fields = ('id', 'company_name', 'engineers')
        
    def get_engineers(self, ojb):
        engineers = ojb.engineer_set.all()
        return EngineerSerializer(engineers, many=True).data
    
    
    

    
    
class CompanySimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Company
        fields = ('id', 'company_name')
    
class EngineerSerializer(serializers.ModelSerializer):
    
    companies = CompanySimpleSerializer(source='company', read_only=True)
    sales_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='sales')
    
    class Meta:
        model= Engineer
        fields = ('id', 'engineer_name', 'companies', 'sales_id', 'engineer_type', 'engineer_status')
        
        
class EngineerSimpleSerializer(serializers.ModelSerializer):
    
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company')
    sales_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='sales')
    
    class Meta:
        model= Engineer
        fields = ('id', 'engineer_name', 'sales_id', 'engineer_type', 'engineer_status', 'company_id')