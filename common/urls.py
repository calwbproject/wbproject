from django.contrib.auth import views as auth_views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from common import views


app_name = 'common'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name = 'common/login.html'),name = 'login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logoutTest/',views.logoutTest, name='logoutTest'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]