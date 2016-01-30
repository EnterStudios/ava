# Django Imports
from django.db.models.signals import post_save
from django.dispatch import receiver
# Python Imports
import datetime
from logging import getLogger
# Local Imports
from ava_core.evaluate.models import EvaluateController, EvaluateTest
from ava_core.evaluate.tasks import task_ava_evaluate_controller_run, task_ava_evaluate_controller_expire

# Logger
logger = getLogger(__name__)


# Implementation
@receiver(post_save, sender=EvaluateController)
def signal_ava_post_save_evaluate_controller(sender, created, instance, **kwargs):
    logger.debug('Signal triggered'
                 ' - signal_ava_post_save_evaluate_controller')
    if instance.status == instance.PENDING:
        if instance.scheduled_type == instance.NOW:
            instance.scheduled_time = datetime.datetime.now() + datetime.timedelta(seconds=1)

        instance.expiry_time = instance.scheduled_time
        if instance.expiry_type == instance.DAY:
            instance.expiry_time += datetime.timedelta(minutes=2)
        elif instance.expiry_type == instance.WEEK:
            instance.expiry_time += datetime.timedelta(weeks=1)
        elif instance.expiry_type == instance.MONTH:
            instance.expiry_time += datetime.timedelta(weeks=4)  # TODO:  Find better way to represent month

        instance.status = instance.PROCESSED
        instance.save()

        task_ava_evaluate_controller_run.apply_async((instance.id,), eta=instance.scheduled_time)
        task_ava_evaluate_controller_expire.apply_async((instance.id,), eta=instance.expiry_time)


@receiver(post_save, sender=EvaluateTest)
def signal_ava_post_save_evaluate_target_profile(sender, created, instance, **kwargs):
    logger.debug('Signal triggered'
                 ' - signal_ava_post_save_evaluate_target_profile')
    if created:
        instance.run_evaluate()
