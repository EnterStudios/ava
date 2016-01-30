# Ensure no clash with future
from __future__ import absolute_import
# Celery Imports
from celery import shared_task
from celery.utils.log import get_task_logger
# Local Imports
from ava_core.organize.models import Person


# Implementation
logger = get_task_logger(__name__)


@shared_task
def task_run_intro_email(person_id):
    logger.debug('Task triggered'
                 ' - organize::task_run_intro_email')
    try:
        person = Person.objects.get(id=person_id)
        if person.run_intro():
            task_run_invite_email.apply_async((person_id,), countdown=10)
    except Person.DoesNotExist:
        logger.debug('Task Error'
                     ' - organize::task_run_intro_email'
                     ' - Person.DoesNotExist')
        return


@shared_task
def task_run_invite_email(person_id):
    logger.debug('Task triggered'
                 ' - organize::task_run_invite_email')
    try:
        person = Person.objects.get(id=person_id)
        person.run_invite()
    except Person.DoesNotExist:
        logger.debug('Task Error'
                     ' - organize::task_run_invite_email'
                     ' - Person.DoesNotExist')
        return
