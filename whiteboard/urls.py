from django.urls import path

from . import views

app_name = 'whiteboard'

urlpatterns = [
    # path('load_overview/', views.Load_overview.as_view(), name='overview'),
    path('details/', views.Load_details.as_view(), name='details'),
    path('engineers/', views.Engineer_info.as_view(), name='engineer_info'),
    path('engineers/<int:pk>', views.Engineer_info.as_view(), name='engineer_info_detail'),
    # path('move_engineer/', views.Move_engineer.as_view(), name='move_engineer'),
    path('companies/', views.Company_info.as_view(), name='company_info'),
    path('companyies/<int:pk>', views.Company_info.as_view(), name='company_info_detail'),
    path('sales/', views.Sales_info.as_view(), name='sales_info'),
    path('overview/', views.Load_overview.as_view(), name='load_overview'),
    path('detail/<int:pk>', views.Load_details.as_view(), name='load_detail'),
]