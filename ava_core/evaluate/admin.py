# Django Imports
from django.contrib import admin
# Local Imports
from ava_core.evaluate.models import EvaluateController
from ava_core.evaluate.models import EvaluateSender
from ava_core.evaluate.models import EvaluateTest
from ava_core.evaluate.models import EvaluateResult
from ava_core.evaluate.models import EvaluateTemplate

admin.site.register(EvaluateController)
admin.site.register(EvaluateSender)
admin.site.register(EvaluateTemplate)
admin.site.register(EvaluateTest)
admin.site.register(EvaluateResult)
