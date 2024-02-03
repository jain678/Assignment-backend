from django.urls import path
from .views import CreateInvestorAPIView,CreateStartupAPIView
urlpatterns = [
    path('create_startup/',CreateStartupAPIView.as_view()),
    path('create_investor/',CreateInvestorAPIView.as_view()),
    
]