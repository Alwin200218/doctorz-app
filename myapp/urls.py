from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('register/<int:id>',views.register,name='register'),
    path('doctorRegister/',views.doctorRegister,name='doctorRegister'),


]