# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from restaurants.models import Restaurant
from django.http import HttpResponse

# Returns a JSON object containing the restaurant object.
def retrieve_restaurant(request, restaurant_id):

    if request.method != "GET":
        return BadRequest("invalid method")

    # Retrieve restaurant object
    restaurant = Restaurant.objects.get(id = restaurant_id)

    # Create a dictionary for the restaurant object
    restaurant_dict = {}

    restaurant_dict['id'] = restaurant.id
    restaurant_dict['name'] = restaurant.name
    restaurant_dict['opens_at'] = restaurant.opens_at
    restaurant_dict['closes_at'] = restaurant.closes_at

    return HttpResponse([restaurant_dict], content_type = 'application/json')
