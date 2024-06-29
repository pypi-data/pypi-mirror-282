import requests
from django.conf import settings

from .helpers import LogSettings

settings: LogSettings = getattr(settings, "LOG_SETTINGS", None)


def post_api_log(log_data: dict, priority: bool = False):
    url = (
        settings.url + "/api/api-log/"
        if not settings.url.endswith("/")
        else settings.url + "api/api-log/"
    )
    headers = {
        "Content-Type": "application/json",
        "content-type": "application/json",
        "x-env-id": settings.env_key,
    }
    query = {"p": "1"} if priority else None

    try:
        requests.post(
            url,
            headers=headers,
            params=query,
            json=log_data,
            timeout=0.0000001,
        )
    except requests.exceptions.ReadTimeout:
        pass


def post_or_put_celery_log(log_data: dict, method: str):
    url = (
        settings.url + "/api/celery-log/"
        if not settings.url.endswith("/")
        else settings.url + "api/celery-log/"
    )
    headers = {
        "Content-Type": "application/json",
        "content-type": "application/json",
        "x-env-id": settings.env_key,
    }

    try:
        requests.request(
            method,
            url,
            headers=headers,
            json=log_data,
            timeout=0.0000001,
        )
    except requests.exceptions.ReadTimeout:
        pass
