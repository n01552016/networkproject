from django.urls import path
from .views import send_email, email_sent, index

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email'),
    path('email_sent/', email_sent, name='email_sent'),
]