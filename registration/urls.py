from django.urls import path
from registration.views import RegisterView
from .views import temview,signup
 
from django.contrib.auth import views as auth_Views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('register',RegisterView,basename='api')

urlpatterns = [
    
    
    path('temp',temview,name='site'),
    path('signup',signup,name="signup"),
    path('login',auth_Views.LoginView.as_view(template_name="login.html"),name="login"),
    path('accounts/logout',auth_Views.LogoutView.as_view(),name="logout"),
    path('settings/changepassword',auth_Views.PasswordChangeView.as_view
         (template_name="changepassword.html"),name="changepassword"),
    path('settings/changepassword/done',auth_Views.PasswordChangeDoneView.as_view
         (template_name="changepassworddone.html"),name="changepassworddone"),   
 
           
] 
urlpatterns=urlpatterns+router.urls