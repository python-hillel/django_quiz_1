from django.contrib import admin

from .models import Choice
from .models import Exam
from .models import Question
from .models import Result

admin.site.register(Choice)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Result)
