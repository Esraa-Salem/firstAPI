from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from rest_framework import viewsets
# Create your views here.
 
class RegisterView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
# class RegisterView(GenericAPIView ):
#     serializer_class=UserSerializer
#     def post(self,request):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
 
def temview(request):
    return render(request,"contact.html")

def signup(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('site')
    return render(request,"signup.html",{'form':form})  

 
