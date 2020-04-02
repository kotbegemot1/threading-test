from time import sleep

from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import ListView, CreateView

from .models import Mail
from .forms import MailForm

# Create your views here.

# def mail_send(request):
#     # send_mail(
#     #     'Subject here',
#     #     'Here is the message.',
#     #     'ivan.banan.2021@mail.ru',
#     #     ['vefof49578@ismailgul.net'],
#     #     fail_silently=False,
#     # )
#     form = MailForm()
#     return render(request, 'mail/index.html', context={'form': form})

# class SendMail(View):
#     def get(self, request):
#         form = MailForm()
#         return render(request, 'mail/index.html', {'form': form})

#     def post(self,request):
#         form = MailForm(request.POST)
#         if form.is_valid():
#             new_form = form.save()
#             # sleep(int(request.POST['delay']))
#             # send_mail(request.POST['subject'], request.POST['text'], 'ivan.banan.2021@mail.ru', [request.POST['mail_adress']], fail_silently=False)
#             return redirect('mails_list_url')
#         return render(request, 'mail/index.html', {'form': form})

class CreateMail(CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mails_list_url')
    template_name = 'mail/index.html'


class MailsList(ListView):
    model = Mail
    template_name = 'mail/mails_list.html'