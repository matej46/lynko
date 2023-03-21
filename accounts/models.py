from django.db import models
from django.contrib.auth.models import AbstractUser
import djstripe
from djstripe.models import Customer, Subscription
# Create your models here.

class plan(models.Model):
    name = models.CharField(max_length=255)
    max_num_links = models.IntegerField()


class User(AbstractUser):
    Plan = models.ForeignKey(plan, related_name='users', default=1, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, blank=True,on_delete=models.SET_NULL)
    