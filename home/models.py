# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Prenoms(models.Model):

    #__Prenoms_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    evt = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    fichier = models.IntegerField(null=True, blank=True)

    #__Prenoms_FIELDS__END

    class Meta:
        verbose_name        = _("Prenoms")
        verbose_name_plural = _("Prenoms")



#__MODELS__END
