from django.urls import path
from registration.views import RegisterView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('register',RegisterView,basename='api')

urlpatterns = [] 
urlpatterns=urlpatterns+router.urls