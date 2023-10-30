#!/usr/bin/python3
"""This module creates a new view for Amenity objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity)
    for amenity in amenities.values():
        return jsonify([amenity.to_dict()])


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    res = storage.get(Amenity, amenity_id)
    if res:
        return jsonify(res.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates a Amenity"""
    rsr = request.get_json()
    if not rsr:
        abort(400, 'Not a JSON')
    if 'name' not in amenity:
        abort(400, 'Missing name')
    amenity = Amenity(**rsr)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """Updates a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    amenity_json = request.get_json()
    if not amenity_json:
        abort(400, 'Not a JSON')
    for k, v in amenity_json.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, k, v)
    storage.save()
    return jsonify(amenity.to_dict()), 200