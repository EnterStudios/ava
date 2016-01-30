from django.db import models

from ava_core.abstract.models import TimeStampedModel


class GatherHistory(TimeStampedModel):
    COMPLETED = 0
    FAILED = 1

    IMPORT_STATUS_TEMPLATE = (
        (COMPLETED, 'Conpleted'),
        (FAILED, 'Failed'),
    )

    import_status = models.IntegerField(choices=IMPORT_STATUS_TEMPLATE,
                                        default=COMPLETED)
    message = models.CharField(max_length=500, null=True)
    no_people = models.IntegerField(null=True, blank=True)
    no_groups = models.IntegerField(null=True, blank=True)
    no_identifiers = models.IntegerField(null=True, blank=True)
    next_scheduled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.created) + " [ " + str(self.message) + " ] "

    @staticmethod
    def get_display_import_status(self, look_up):
        return self.IMPORT_STATUS_TEMPLATE[look_up]

    class Meta:
       ordering = ['-created']

