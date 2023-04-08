from chat.views import text_chat
from django.urls import path, include

urlpatterns = [
    path("textChat", text_chat),
]
