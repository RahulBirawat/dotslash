"""
URL configuration for JHBFVDJSB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("form/",views.form),
    path("predict/", views.predict),
    path("predict_1/",views.predict_1),
    path("predict_2/",views.predict_2),
    path("predict/result", views.result),
    path("predict_1/result_1",views.result_1),
    path("predict_2/result_2",views.result_2),
    path("predict/form/",views.recommender)
]
