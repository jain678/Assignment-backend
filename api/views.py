from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Startup,Investor
from django.shortcuts import get_object_or_404
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
    
class getStartupAPIView(APIView):
    def get(self,request, format = None):
        startups = Startup.objects.all()
        startup_dict = {}

        for i in startups:
            id = i.id
            company_name = i.company_name
            desc = i.business_description
            rev = i.revenue
            startup_dict[f'{id}'] = {'company_name': company_name,'id':id,'business_description':desc,'revenue':rev}
        response = Response(startup_dict)
        return response
    
class ShowInterestAPIView(APIView):
    def post (self, request,pk, format = None):
        response = Response()
        try:
            startup = get_object_or_404(Startup, id = pk)
            startup.interested.add(request.user)
            response.data = {
                'msg':'success'
            }
        except:
            response.data = {
                'msg':'failed'
            }
        return response
        
        
