from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializers import UserSerializer

# Create your views here.
# Logout feature
def logoutTest(request):
    return render(request, 'common/index.html')

class UserView(APIView):
    #postの要請を処理してユーザを作成する
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)