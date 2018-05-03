# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

# Restaurant model represents table structure of the SQLite database. ID field is automatically createed.
class Restaurant(models.Model):

    name = models.CharField(_('name'), max_length=500, null=False, blank=False, db_index=True)
    opens_at = models.TimeField(_('opens at'))
    closes_at = models.TimeField(_('closes at'))

    #for system/migration notes
    _notes = models.CharField(_('_notes'), max_length=100, null=True, default=None)
