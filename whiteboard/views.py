from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from whiteboard.serializers import CompanySerializer

# Create your views here.
# 概要のロード	
# 詳細のロード	
# エンジニア登録	
# エンジニア修正	
# エンジニア移動	
# 会社登録	
# 会社削除	
# 会社確認


#개요 조회
class Load_overview(APIView):
    pass

#상세 조회
class Load_details(APIView):
    pass

#엔지니어 정보 관련 클래스
class Engineer_info(APIView):
    
    
    #엔지니어 등록
    def post(self, request):
        return Response({'result':'post'}, status=status.HTTP_201_CREATED)
    
    #엔지니어 수정
    def update(self, request):
        return Response({'result':'update'}, status=status.HTTP_201_CREATED)
    
    #엔지니어 삭제
    def delete(self, request):
        return Response({'result':'delete'}, status=status.HTTP_201_CREATED)
    
    #엔지니어 조회
    def get(self, request):
        
        serializer = CompanySerializer(data = request.data)
        
        return Response({'result':'get'}, status=status.HTTP_201_CREATED)
    

#회원을 다른 회사로 이동
class Move_engineer(APIView):
    pass




#회사 CRUD
class Company_info(APIView):
    # 회사 조회
    def get(self, request, pk):
        return Response({'result':'get'}, status=status.HTTP_201_CREATED)
    
    # 회사 등록
    def post(self, request):
        return Response({'result':'post'}, status=status.HTTP_201_CREATED)
    
    #회사 삭제
    def delete(self, request):
        return Response({'result':'delete'}, status=status.HTTP_201_CREATED)
    
    #회사 수정
    def update(self, request):
        return Response({'result':'update'}, status=status.HTTP_201_CREATED)
    