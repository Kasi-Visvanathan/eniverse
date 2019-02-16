from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name = "home"),
	path('loggedin/',views.loggedin,name="loggedin"),
	path('signup/',views.signup,name="signup"),
	path('signup/registered/',views.registered, name="registered")

]