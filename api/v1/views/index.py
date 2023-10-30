#!/usr/bin/python3
"""
Creates a route /status on the object app_views that returns a JSON status
"""
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns a JSON status"""
    return {"status": "OK"}
