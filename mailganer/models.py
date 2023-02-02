# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.email) + ' ' + str(self.first_name) + ' ' + str(self.last_name)
