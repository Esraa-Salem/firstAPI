from django.urls import path
from registration.views import UserSerializerlist ,UserINFO
from rest_framework.routers import DefaultRouter
from .views import registerapi,user_logout
from knox import views as views_knox
from .views import loginapi
# router=DefaultRouter()
# router.register('register',RegisterView,basename='api')

urlpatterns = [
    path('getall/',UserSerializerlist.as_view(),name='get'),
    path("details/<int:id>/",UserINFO.as_view()),
    path('register/',registerapi.as_view(),name='register'),
    path('login/',loginapi.as_view(),name='login'),
    path('logout/',user_logout,name='logout'),
    #path('logoutall/',views_knox.LogoutAllView.as_view(),name='logoutall')
] 
#urlpatterns=urlpatterns+router.urls
 