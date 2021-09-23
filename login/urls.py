from .views import login,home
from django.urls import path
app_name='login'
urlpatterns = [
    path("login/",login,name='login'),
    path('',home,name='home')
]
