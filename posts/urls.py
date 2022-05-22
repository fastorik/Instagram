from cgitb import lookup
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('instagram', views.PostViewSet,
                basename='post')

urlpatterns = [
    path('', include(router.urls))
]

