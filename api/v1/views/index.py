#!/usr/bin/python3
""" Module for status """

from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route("/status", strict_slashes=False)
def status_ok():
    """ returns a JSON """
    obj = {"status": "OK"}
    return jsonify(obj)
