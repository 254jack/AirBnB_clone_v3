#!/usr/bin/python3

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def get_status():
	"""Get the status of the API"""
	return jsonify({"status": "OK"})
