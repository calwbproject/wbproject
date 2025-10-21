from rest_framework import serializers

from whiteboard.models import Company, Engineer

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Company
        fields = ('id', 'company_name')
    
class EngineerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Engineer
        fields = ('id', 'engineer_name', 'company_name', 'sales_name', 'engineer_type')