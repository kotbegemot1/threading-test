from django.urls import path
from .views import *

urlpatterns = [
    # path('', mail_send, name='send_mail'),
    # path('', SendMail.as_view(), name='send_mail'),
    path('', CreateMail.as_view(), name='send_mail'),
    path('mails/', MailsList.as_view(), name='mails_list_url'),
]