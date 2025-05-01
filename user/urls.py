from django.contrib import admin
from django.urls import path, include

from user.views import UserViewSet, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", UserViewSet.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
