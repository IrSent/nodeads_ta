from django.contrib import admin

from question.models import Question
from question.models import Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_on', 'get_likes']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'text', 'created_on', 'get_likes']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
