# Django Imports
from django.db.models.signals import post_save
from django.dispatch import receiver
# Python Imports
from logging import getLogger
# Local Imports
from .models import Person, PersonAttribute, PersonIdentifier, PersonIdentifierAttribute, GroupIdentifier, \
    GroupIdentifierAttribute

# Logging
logger = getLogger(__name__)


# Implementation
@receiver(post_save, sender=Person)
def signal_ava_organize_person_post_save(sender, created, instance, **kwargs):
    logger.debug('Signal Called'
                 '- organize::signal_ava_organize_person_post_save')
    if created:
        logger.debug('Signal Fired'
                     ' - organize::signal_ava_organize_person_post_save')
        attribute = PersonAttribute.objects.create(person=instance)
        attribute.save()


@receiver(post_save, sender=PersonIdentifier)
def signal_ava_organize_person_identifier_post_save(sender,created, instance, **kwargs):
    logger.debug('Signal Called'
                 '- organize::signal_ava_organize_person_identifier_post_save')
    if created:
        logger.debug('Signal Fired'
                     ' - organize::signal_ava_organize_person_identifier_post_save')
        attribute = PersonIdentifierAttribute.objects.create(identifier=instance)
        attribute.save()


@receiver(post_save, sender=GroupIdentifier)
def signal_ava_organize_group_identifier_post_save(sender,created, instance, **kwargs):
    logger.debug('Signal Called'
                 '- organize::signal_ava_organize_group_identifier_post_save')
    if created:
        logger.debug('Signal Fired'
                     ' - organize::signal_ava_organize_group_identifier_post_save')
        attribute = GroupIdentifierAttribute.objects.create(identifier=instance)
        attribute.save()
