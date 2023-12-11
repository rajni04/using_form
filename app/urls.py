

from django.urls import path
from .views import *


urlpatterns = [
    path("sign_in/", sign_in, name="sign_in"),
    path("register/", register, name="register"),
    path("update_std/<int:pk>/", update_std, name="update_std"),
    path("addclass/", addClass, name="addclass"),
    path("logout_view/", logout_view, name="logout_view"),
    path("", home),




    ]