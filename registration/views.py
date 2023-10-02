from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token 
# Create your views here.
 

class UserSerializerlist(APIView):
   
    def get(self,request):
        users=User.objects.all()
        data=UserSerializer(users,many=True).data
        return Response(data)
    
    def post(self,request):

        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':404,'errors':serializer.errors,'msg':'not found'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj , _ =Token.objects.get_or_create(user=user)
           
        return Response({'status':200,'msg':'created success','token':str(token_obj)} )

       # try:
        #     if  serializer.is_valid():
        #         serializer.save()
        #         user=User.objects.get(username=serializer.data['username'])
        #         token_obj , _ =Token.objects.get_or_create(user=user)
           
        #         return Response({'status':200,'msg':'created success','token':str(token_obj)} )
        # except:
        
        #      return Response({'status':404,'errors':serializer.errors,'msg':'created failed'})

class UserINFO(APIView): 
    
    def get(self,request,id):
        try:
            users=User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'status':404,'errors':serializer.errors,'msg':'not found'} )
        serializer=UserSerializer(users)
        
        return Response({'status':200,'data':serializer.data,'msg':'created success'})
       
 
    def put(self,request,id):
          try:
            users=User.objects.get(id=id)
          except User.DoesNotExist:
            return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
          serializer=UserSerializer(users,data=request.data)
          try:
            if serializer.is_valid():
                serializer.save()
             
                return Response({'status':200,'msg':'Updated successfully'} )
          except:
        
             return Response({'status':404,'errors':serializer.errors,'msg':'Updated failed'} )
          
    def delete(self,request,id):
         try:
            users=User.objects.get(id=id)
         except User.DoesNotExist:
            return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
         users.delete()
         return Response({'status':200,'msg':'deleted is done'} )

    