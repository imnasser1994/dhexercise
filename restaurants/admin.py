# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from restaurants.models import Restaurant


# Admin page class, allows manipulation of the Restaurant table data
class RestaurantAdmin(admin.ModelAdmin):

    # fields to display on the Add/Edit article page
    fields = ['id', 'name', 'opens_at', 'closes_at']

    # fields to display on the View articles page (changelist)
    list_display = ['id', 'name', 'opens_at', 'closes_at']

    # fields designated as readonly on Add/Edit
    readonly_fields = ['id']

    # fields to check for on searching for a string
    search_fields = ['name']

# Activates the admin page within the admin panel.
admin.site.register(Restaurant, RestaurantAdmin)
