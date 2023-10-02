from django.urls import path
from registration.views import UserSerializerlist ,UserINFO
from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register('register',RegisterView,basename='api')

urlpatterns = [
    path('',UserSerializerlist.as_view(),name='get'),
    path("details/<int:id>/",UserINFO.as_view()),
   
] 
#urlpatterns=urlpatterns+router.urls
 