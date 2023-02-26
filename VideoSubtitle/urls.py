from django.urls import path

from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('videos/', views.index),
    # path('videos/', views.showvideo)
]