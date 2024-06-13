#!/usr/bin/python3
""" Module for status """

from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route("/status", strict_slashes=False)
def status_ok():
    """ returns a JSON """
    obj = {"status": "OK"}
    return jsonify(obj)


@app_views.route("/api/vi/stats", stict_slashes=False)
def count_obj():
    """ Retrieves the number of each objects by type. """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")
                    })
