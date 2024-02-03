from django.urls import path
from .views import CreateInvestorAPIView,CreateStartupAPIView, getStartupAPIView, ShowInterestAPIView
urlpatterns = [
    path('create_startup/',CreateStartupAPIView.as_view()),
    path('create_investor/',CreateInvestorAPIView.as_view()),
    path('startups_list/', getStartupAPIView.as_view()),     
    path('interested/<int:pk>', ShowInterestAPIView.as_view()),  
]