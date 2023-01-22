from django.urls import path
from rest_framework import routers

from ads.views.selection import SelectionViewSet
urlpatterns = []

router = routers.SimpleRouter()
router.register('', SelectionViewSet)

urlpatterns += router.urls