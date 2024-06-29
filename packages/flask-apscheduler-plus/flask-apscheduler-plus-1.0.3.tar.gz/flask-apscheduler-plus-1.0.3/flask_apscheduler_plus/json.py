# -*- coding: utf-8 -*-
import flask
import datetime

from apscheduler.job import Job
from flask_apscheduler_plus.utils import job_to_dict

import json  # noqa

loads = json.loads


def dumps(obj, indent=None):
    return json.dumps(obj, indent=indent, cls=JSONEncoder)


def jsonify(data, status=None):
    indent = None
    if flask.current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not getattr(flask.request, "is_xhr"):
        indent = 2
    return flask.current_app.response_class(dumps(data, indent=indent), status=status, mimetype='application/json')


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        if isinstance(obj, Job):
            return job_to_dict(obj)

        return super(JSONEncoder, self).default(obj)
