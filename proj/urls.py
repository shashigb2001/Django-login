
from django.contrib import admin
from django.urls import path
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page ,name="login_page"),
    path('register/', register, name="register"),
    path('logout/', logout_page, name="logout_page"),

    path('home/', home, name="home_page"),

]
