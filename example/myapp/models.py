from django.db import models
from localflavor.us.models import PhoneNumberField


class Foo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bar(models.Model):
    foo = models.ForeignKey('Foo')
    number = PhoneNumberField('phone number')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.number
