import stat
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.serializers import UserSerializer
from whiteboard.models import Company, Engineer
from whiteboard.serializers import CompanySerializer, CompanySimpleSerializer, EngineerSerializer, EngineerSimpleSerializer


#Retrive overview
class Load_overview(APIView):
    def get(self, request):
        #get user data
        user = User.objects.exclude(username='admin')
        
        #transfer to json
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#Retrive detail
class Load_details(APIView):
    def get(self, request, pk):
        
        #check pk existence
        if pk is None:
            return Response({'data':'pk in blank'},status=status.HTTP_400_BAD_REQUEST)
        
        #get user data
        user = User.objects.get(pk=pk)
        
        #transfer to json
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

#Engineer-related class
class Engineer_info(APIView):
    
     #get engineer data
    def get(self, request, pk=None):
        
        # select all or selected by ID, depending on whether pk exists
        if pk is None:
            #get data
            engineers = Engineer.objects.all();
            #serialize object
            serializer = EngineerSerializer(engineers, many=True)
            
        #get specific engineer
        else:
            #get data
            engineers = Engineer.objects.get(pk=pk)
            #serialize object
            serializer = EngineerSerializer(engineers)
        # TODO : need to set up error page handling
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #insert a new ngineer
    def post(self, request):
        
        serializer = EngineerSerializer(data=request.data)
        
        #if data is valid
        if serializer.is_valid():
            
            engineer = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # when data isn't valid
        else:
            print(serializer.error)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
    #delete engineer
    def delete(self, request, pk):
        #if request is valid
        if pk is not None:
            engineer = get_object_or_404(Engineer, pk=pk)
            engineer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        #return if pk is None
        return Response({'detail':'no id provied'}, status=status.HTTP_400_BAD_REQUEST)
    
     #엔지니어 수정
    def put(self, request, pk=None):
        # 입력값이 없으면 오류
        print(request.data)
        if pk is None:
            return Response({'data':'pk is None'}, status=status.HTTP_400_BAD_REQUEST)
        
        #업데이트 시작
        #인스턴스 조회
        engineer = get_object_or_404(Engineer, pk=pk)
        
        #시리얼라이저 생성
        serializer = EngineerSimpleSerializer(engineer, data=request.data, partial=True)
        
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
            serializer = CompanySimpleSerializer(companies, many=True)
            
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
    

#retrieval user data
class Sales_info(APIView):
    
    def get(self, request):
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)