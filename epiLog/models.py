'''
    epiLog: an object annotation system
    Copyright 2012 Martin Paul Eve

    This file is part of epiLog.

    epiLog is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    epiLog is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with epiLog. If not, see <http://www.gnu.org/licenses/>.

'''

from django.db import models
from userprofile.models import BaseProfile
from django.utils.translation import ugettext as _
from django.conf import settings
import datetime

GENDER_CHOICES = [ ('U', _('Unspecified')), ('F', _('Female')), ('M', _('Male')), ('O', _('Other'))]

class UserProfileInfo(BaseProfile):
    firstname = models.CharField(max_length=255, blank=True, verbose_name="First name")
    surname = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(default=datetime.date.today(), blank=True, verbose_name="Birthdate (YYYY-MM-DD)")
    url = models.URLField(blank=True)
    about = models.TextField(blank=True)