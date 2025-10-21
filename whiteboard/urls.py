from django.urls import path

from . import views

app_name = 'whiteboard'

urlpatterns = [
    path('load_overview/', views.Load_overview.as_view(), name='overview'),
    path('load_details/', views.Load_details.as_view(), name='details'),
    path('engineer_info/', views.Engineer_info.as_view(), name='engineer_info'),
    path('engineer_info/<int:pk>', views.Engineer_info.as_view(), name='engineer_info_detail'),
    path('move_engineer/', views.Move_engineer.as_view(), name='move_engineer'),
    path('company_info/', views.Company_info.as_view(), name='company_info'),
    path('company_info/<int:pk>', views.Company_info.as_view(), name='company_info_detail'),
]