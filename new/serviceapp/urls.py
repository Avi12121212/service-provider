from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('service/',views.service),
    # path('worker/', views.worker),
    path('user/', views.user),
    path("main/", views.main),
    path('logout/', views.logout),
]
