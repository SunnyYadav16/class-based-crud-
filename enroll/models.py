from django.db import models

# Create your models here.
from django.urls import reverse, reverse_lazy


class UserData(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    """ For redirecting to a particular url from the models part without giving success urls in views"""
    # def get_absolute_url(self):
    #     return reverse_lazy("thanks")

    """ For showing the data as soon as the object is created on another page """
    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"pk": self.pk})