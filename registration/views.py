from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import viewsets,generics,permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token 
# Create your views here.
from knox.models import AuthToken
from knox.views import LoginView as knoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
class registerapi(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= serializer.save()
        return Response({
            'status':200,'msg':'created success',
            'token':AuthToken.objects.create(user)[1]
        })

class loginapi(knoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post (self,request,format=None):
         serializer=AuthTokenSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         user=serializer.validated_data['user']
         login(request,user)
         return super(loginapi,self).post(request,format=None)


 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.delete()
            return Response({'status':200,'message': 'Successfully logged out.'})
        except Exception as e:
            return Response({'status':400,'error': str(e)})

 
class UserSerializerlist(APIView):
     
     def get(self,request):
         users=User.objects.all()
         data=UserSerializer(users,many=True).data
         return Response(data)
    
#     def post(self,request):

#         serializer=UserSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'status':404,'errors':serializer.errors,'msg':'not found'})
#         serializer.save()
#         user=User.objects.get(username=serializer.data['username'])
#         token_obj , _ =Token.objects.get_or_create(user=user)
           
#         return Response({'status':200,'msg':'created success','token':str(token_obj)} )

#        # try:
#         #     if  serializer.is_valid():
#         #         serializer.save()
#         #         user=User.objects.get(username=serializer.data['username'])
#         #         token_obj , _ =Token.objects.get_or_create(user=user)
           
#         #         return Response({'status':200,'msg':'created success','token':str(token_obj)} )
#         # except:
        
#         #      return Response({'status':404,'errors':serializer.errors,'msg':'created failed'})

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
          
           if serializer.is_valid():
                 serializer.save()
             
                 return Response({'status':200,'msg':'Updated successfully'} )
          
        
           return Response({'status':404,'errors':serializer.errors,'msg':'Updated failed'} )
          
     def delete(self,request,id):
          try:
             user=User.objects.get(id=id)
          except User.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
        
          user.delete()
          return Response({'status':200,'msg':'deleted is done'} )

    