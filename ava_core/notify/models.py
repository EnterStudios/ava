import logging

from django.db import models

from ava_core.abstract.models import ReferenceModel

log = logging.getLogger(__name__)


class NotificationEmail(ReferenceModel):
    INTRO = 0
    INVITE = 1
    UPDATED = 2
    ACHIEVEMENT = 3
    PASS = 4
    FAIL = 5

    NOTIFICATION_TYPE_CHOICES = (
        (INTRO, 'Introducing AVA'),
        (INVITE, 'Invitation to join AVA'),
        (UPDATED, 'Update to your profile'),
        (ACHIEVEMENT, 'Achievement Unlocked'),
        (PASS, 'Test Completed - Success!'),
        (FAIL, 'Test Completed - Failure'),

    )
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPE_CHOICES,
                                            default=INTRO,
                                            unique=True,
                                            verbose_name='Notification Type')
    address_from = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    @staticmethod
    def get_display_notification_type(self, look_up):
        return self.NOTIFICATION_TYPE_CHOICES[look_up]
