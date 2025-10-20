from rest_framework import serializers

from whiteboard.models import Company, Engineer

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Company
        fields = ('id', 'company_name')
    
class Engineer(serializers.ModelSerializer):
    
    class Meta:
        model= Engineer
        field = ('id', 'engineer_name', 'company_name', 'sales_name', 'engineer_type')