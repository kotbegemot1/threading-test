from django.db import models

from django.core.mail import send_mail

import threading
from time import sleep

# Create your models here.

class Mail(models.Model):
    subject = models.CharField("Тема", max_length=50, db_index=True)
    text = models.TextField("Текст сообщения")
    mail_adress = models.EmailField("Введите Email получателя")
    delay = models.SmallIntegerField("Задержка")
    is_send = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Mail, self).save(*args, **kwargs)
            
        def send_mail_delay(*args, **kwargs):
            sleep(self.delay)
            send_mail(self.subject, self.text, 'ivan.banan.2021@mail.ru', [self.mail_adress], fail_silently=False,)
            self.is_send = True
            super(Mail, self).save()

        t = threading.Thread(
            target=send_mail_delay, 
            args=(self.subject, self.text, self.mail_adress, self.delay, self)
        )
        t.start()