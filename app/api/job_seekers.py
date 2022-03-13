#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
import requests
import json
from app.constants.globals import *

URL = f"{BACKEND_HOST}/job-seeker"


class JobSeekersService(object):

    @classmethod
    def add_job_seekers(cls, **kwargs):
        url = f"{URL}"
        response = requests.post(url, json=json.dumps(kwargs))
        return response

    @classmethod
    def update_job_seekers(cls, **kwargs):
        url = f"{URL}"
        response = requests.put(url, json=json.dumps(kwargs))
        return response

    @classmethod
    def filter_table(cls, **kwargs):
        url = f"{URL}/filter-table"
        data = json.dumps(kwargs)
        response = requests.post(url, json=data, params=data)
        return response

    @classmethod
    def delete(cls, job_seeker_id):
        url = f"{URL}/{job_seeker_id}"
        response = requests.delete(url)
        return response

    @classmethod
    def get_by_id(cls, job_seeker_id):
        url = f"{URL}/{job_seeker_id}"
        response = requests.get(url)
        return response

    @classmethod
    def update_experiences(cls, **kwargs):
        url = f"{URL}/experiences"
        response = requests.put(url, json=json.dumps(kwargs))
        return response

    @classmethod
    def update_awards(cls, **kwargs):
        url = f"{URL}/awards"
        response = requests.put(url, json=json.dumps(kwargs))
        return response

    @classmethod
    def filter_table_less(cls, **kwargs):
        url = f"{URL}/filter-table-less"
        data = json.dumps(kwargs)
        response = requests.post(url, json=data, params=data)
        return response

    @classmethod
    def evaluate_job_seeker(cls, **kwargs):
        url = f"{URL}/evaluate"
        response = requests.put(url, json=json.dumps(kwargs))
        return response

    @classmethod
    def activate_job_seeker(cls, job_seeker_code, confirm_number):
        url = f"{URL}/{job_seeker_code}/active-job-seeker/{confirm_number}"
        response = requests.get(url)
        return response

    @classmethod
    def export_excel(cls, **kwargs):
        pass
