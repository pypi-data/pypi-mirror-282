# -*- coding: utf-8 -*-
import logging
from collections import OrderedDict
from flask import current_app, request, jsonify
from apscheduler.jobstores.base import ConflictingIdError, JobLookupError

from flask_apscheduler_plus.utils import job_to_dict

logger = logging.getLogger('flask_apscheduler')


def get_scheduler_info():
    """Gets the scheduler info."""

    scheduler = getattr(current_app, "apscheduler")

    d = OrderedDict([
        ('current_host', scheduler.host_name),
        ('allowed_hosts', scheduler.allowed_hosts),
        ('running', scheduler.running)
    ])

    return jsonify(dict(code=200101, message="successful", data=d)), 200


def add_job():
    """Adds a new job."""

    data = request.get_json(force=True)

    try:
        apscheduler = getattr(current_app, "apscheduler")
        job = apscheduler.add_job(**data)
        return jsonify(dict(code=200101, message="successful", data=job_to_dict(job))), 200
    except ConflictingIdError:
        string = 'Job %s already exists.' % data.get('id')
        logger.error(string)
        return jsonify(dict(code=400101, message=string, data=None)), 400
    except Exception as e:
        logger.error(e)
        return jsonify(dict(code=500101, message=str(e), data=None)), 500


def delete_job(job_id: str):
    """Deletes a job."""

    try:
        apscheduler = getattr(current_app, "apscheduler")
        apscheduler.remove_job(job_id)
        return jsonify(dict(code=200101, message="successful", data=None)), 200
    except JobLookupError:
        string = 'Job %s not found.' % job_id
        logger.error(string)
        return jsonify(dict(code=400102, message=string, data=None)), 400
    except Exception as e:
        logger.error(e)
        return jsonify(dict(code=500101, message=str(e), data=None)), 500


def get_job(job_id: str):
    """Gets a job."""
    apscheduler = getattr(current_app, "apscheduler")
    job = apscheduler.get_job(job_id)

    if not job:
        string = 'Job %s not found.' % job_id
        logger.error(string)
        return jsonify(dict(code=400102, message=string, data=None)), 400

    return jsonify(dict(code=200101, message="successful", data=job_to_dict(job))), 200


def get_jobs():
    """Gets all scheduled jobs."""
    apscheduler = getattr(current_app, "apscheduler")
    jobs = apscheduler.get_jobs()
    job_states = []
    for job in jobs:
        job_states.append(job_to_dict(job))
    return jsonify(dict(code=200101, message="successful", data=job_states)), 200


def update_job(job_id: str):
    """Updates a job."""

    data = request.get_json(force=True)

    try:
        apscheduler = getattr(current_app, "apscheduler")
        apscheduler.modify_job(job_id, **data)
        job = apscheduler.get_job(job_id)
        return jsonify(dict(code=200101, message="successful", data=job_to_dict(job))), 200
    except JobLookupError:
        string = 'Job %s not found.' % job_id
        logger.error(string)
        return jsonify(dict(code=400102, message=string, data=None)), 400
    except Exception as e:
        logger.error(e)
        return jsonify(dict(code=500101, message=str(e), data=None)), 500


def pause_job(job_id: str):
    """Pauses a job."""

    try:
        apscheduler = getattr(current_app, "apscheduler")
        apscheduler.pause_job(job_id)
        job = apscheduler.get_job(job_id)
        return jsonify(dict(code=200101, message="successful", data=job_to_dict(job))), 200
    except JobLookupError:
        string = 'Job %s not found.' % job_id
        logger.error(string)
        return jsonify(dict(code=400102, message=string, data=None)), 400
    except Exception as e:
        logger.error(e)
        return jsonify(dict(code=500101, message=str(e), data=None)), 500


def resume_job(job_id: str):
    """Resumes a job."""

    try:
        apscheduler = getattr(current_app, "apscheduler")
        apscheduler.resume_job(job_id)
        job = apscheduler.get_job(job_id)
        return jsonify(dict(code=200101, message="successful", data=job_to_dict(job))), 200
    except JobLookupError:
        string = 'Job %s not found.' % job_id
        logger.error(string)
        return jsonify(dict(code=400102, message=string, data=None)), 400
    except Exception as e:
        logger.error(e)
        return jsonify(dict(code=500101, message=str(e), data=None)), 500


def run_job(job_id: str):
    """Executes a job."""

    try:
        apscheduler = getattr(current_app, "apscheduler")
        apscheduler.run_job(job_id)
        job = apscheduler.get_job(job_id)
        return jsonify(dict(code=200101, message="successful", data=job_to_dict(job))), 200
    except JobLookupError:
        string = 'Job %s not found.' % job_id
        logger.error(string)
        return jsonify(dict(code=400102, message=string, data=None)), 400
    except Exception as e:
        logger.error(e)
        return jsonify(dict(code=500101, message=str(e), data=None)), 500
