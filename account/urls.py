from django.urls import path
from account import views
from account.serializers import UserSerializer

urlpatterns = [
    path('users/',views.user_list),

]