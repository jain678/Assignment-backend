from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Startup,Investor
# Create your views here.

class CreateInvestorAPIView(APIView):
    def post(self,request,format=None):
        data = request.data
        username=data['username']
        email=data['email']
        password=data['password']
        # print(username)
        # print(email)
        #create user first as investor
        user = User(username=username,password=password)
        user.save()

        #now give email to investor
        investor = Investor(user=user,email=email)
        investor.save()
        response=Response({"message":"Investor Created Successfully"})
        return response

class CreateStartupAPIView(APIView):
    def post(self,request,format=None):
        data = request.data
        username=data['username']
        email=data['email']
        password=data['password']
        company_name = data['company_name']
        business_description = data['business_description']
        revenue = data['revenue']

        #create user first
        user = User(username=username,password=password)
        user.save()

        startup = Startup(user=user,email=email,company_name=company_name,business_description=business_description,revenue=revenue)
        
        startup.save()
        response=Response({"message":"StartUP Created Successfully"})
        return response