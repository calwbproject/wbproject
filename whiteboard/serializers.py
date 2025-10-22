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
    
    company = CompanySimpleSerializer(source='company_name', read_only=True)
    
    class Meta:
        model= Engineer
        fields = ('id', 'engineer_name', 'company', 'sales_name', 'engineer_type')