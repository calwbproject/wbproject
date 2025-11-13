from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from common.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

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


# KIM
# Login logic
class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        res = super().post(request, *args, **kwargs)
        response = Response("generate token success")
        ac = res.data.get('access', None)
        response.headers["Authorization"] = "Bearer " + ac
        response.set_cookie("refresh", res.data.get('refresh', None))
        # httponly=True, secure=True, 
        return response
    
class RefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        # request.data는 QueryDict일 수 있으니 안전하게 복사본 사용
        data = request.data.copy()
        if not data.get("refresh"):
            cookie_refresh = request.COOKIES.get("refresh")
            if cookie_refresh:
                data["refresh"] = cookie_refresh

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data 

        # 응답 생성
        res = Response("refresh success", status=status.HTTP_200_OK)

        # access는 헤더로 전달
        access = tokens.get("access")
        res.headers["access"] = access

        # refresh 회전(rotate) 설정이 켜져 있다면 새 refresh가 반환됨 -> 쿠키 갱신
        new_refresh = tokens.get("refresh")
        if new_refresh:
            res.set_cookie(
                "refresh", new_refresh,
                samesite="None", path="/api/token/refresh/",
                # httponly=True, secure=True, 
            )

        return res