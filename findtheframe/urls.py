from django.urls import path, include
from rest_framework import routers

from .views.bot import BotView

router = routers.DefaultRouter()
router.register(r'bot', BotView, basename='bot')

urlpatterns = [
    path('', include(router.urls)),
]