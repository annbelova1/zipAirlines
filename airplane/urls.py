from django.conf.urls import url
from django.urls import include

from rest_framework import routers
from airplane.views import AirlineApiView

router = routers.DefaultRouter()
router.register(r'', AirlineApiView, basename='airplanes')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
