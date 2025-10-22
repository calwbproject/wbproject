import stat
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.serializers import UserSerializer
from whiteboard.models import Company, Engineer
from whiteboard.serializers import CompanySerializer, EngineerSerializer

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
    def get(self, request):
        #유저 정보 조회
        user = User.objects.all()
        
        #json 변환
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#상세 조회
class Load_details(APIView):
    def get(self, request, pk):
        
        #pk가 입력이 있는지 없는지 확인
        if pk is None:
            return Response({'data':'pk in blank'},status=status.HTTP_400_BAD_REQUEST)
        
        #유저 정보 조회
        user = User.objects.get(pk=pk)
        
        #json 변환
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

#엔지니어 정보 관련 클래스
class Engineer_info(APIView):
    
     #엔지니어 조회
    def get(self, request, pk=None):
        
        # ID 유무에 따라서 전체 조회, 단일 조회 구분
        if pk is None:
            #데이터 조회
            engineers = Engineer.objects.all();
            #객체를 시리얼라이저
            serializer = EngineerSerializer(engineers, many=True)
            
        #특정 사람 조회
        else:
            #데이터 조회
            engineers = Engineer.objects.get(pk=pk)
            #객체를 시리얼라이저
            serializer = EngineerSerializer(engineers)
        # TODO : 오류 페이지 전송 설정 필요
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #엔지니어 등록
    def post(self, request):
        
        serializer = EngineerSerializer(data=request.data)
        
        #데이터가 정상적일 경우
        if serializer.is_valid():
            
            engineer = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 데이터가 정상적이지 않은 경우
        else:
            print(serializer.error)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
    #엔지니어 삭제
    def delete(self, request, pk):
        #입력 값이 정상적으로 입력이 됐으면
        if pk is not None:
            engineer = get_object_or_404(Engineer, pk=pk)
            engineer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        #pk가 제공이 안됐을 경우 에러 페이지를 반환
        return Response({'detail':'no id provied'}, status=status.HTTP_400_BAD_REQUEST)
    
     #엔지니어 수정
    def put(self, request, pk=None):
        
        # 입력값이 없으면 오류
        if pk is None:
            return Response({'data':'pk is None'}, status=status.HTTP_400_BAD_REQUEST)
        
        #업데이트 시작
        #인스턴스 조회
        engineer = get_object_or_404(Engineer, pk=pk)
        
        #시리얼라이저 생성
        serializer = EngineerSerializer(engineer, data=request.data)
        
        #정상적인경우
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        #정상적이지 않은 경우
        return Response({'data':'pk required for partial update'}, status= status.HTTP_400_BAD_REQUEST)
    

#회원을 다른 회사로 이동
class Move_engineer(APIView):
    pass




#회사 CRUD
class Company_info(APIView):
    # 회사 조회
    def get(self, request, pk=None):
        
        # ID 유무에 따라서 전체 조회, 단일 조회 구분
        if pk is None:
            #객체 조회 후 저장
            companies = Company.objects.all()
            
            #데이터를 시리얼라이저
            # TODO : 예외 처리 필요
            serializer = CompanySerializer(companies, many=True)
            
        else:
            
            #객체 조회 후 저장
            companies = Company.objects.get(pk=pk)
            
            #데이터를 시리얼라이저
            # TODO : 예외 처리 필요
            serializer = CompanySerializer(companies)
            
            
        # TODO : 예외 발생 시 오류 전송 설정 필요
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 회사 등록
    def post(self, request):
        
        serializer = CompanySerializer(data=request.data)
        
        #데이터가 정상적일 경우
        if serializer.is_valid():
            
            company = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 데이터가 정상적이지 않은 경우
        else:
            print(serializer.error)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       
    
    #회사 삭제
    def delete(self, request, pk=None):
        
        #입력 값이 정상적으로 입력이 됐으면
        if pk is not None:
            company = get_object_or_404(Company, pk=pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        #pk가 제공이 안됐을 경우 에러 페이지를 반환
        return Response({'detail':'no id provied'}, status=status.HTTP_400_BAD_REQUEST)
    
    #회사 수정
    def put(self, request, pk=None):
        
        # 입력값이 없으면 오류
        if pk is None:
            return Response({'data':'pk is None'}, status=status.HTTP_400_BAD_REQUEST)
        
        #업데이트 시작
        #인스턴스 조회
        company = get_object_or_404(Company, pk=pk)
        
        #시리얼라이저 생성
        serializer = EngineerSerializer(company, data=request.data)
        
        #정상적인경우
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        #정상적이지 않은 경우
        return Response({'data':'pk required for partial update'}, status= status.HTTP_400_BAD_REQUEST)
    

#영업 분들의 정보 조회
class Sales_info(APIView):
    
    def get(self, request):
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)