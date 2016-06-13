from django.conf.urls import url

from question import api

urlpatterns = [
    url(r'^questions/$', api.question_list_or_post, name='api-question-list-or-post'),
    url(r'^questions/(?P<pk>[0-9]+)/$', api.question_get_edit_delete, name='api-question-get-edit-delete'),
    url(r'^answers/$', api.answer_list_or_post, name='api-answer-list-or-post'),
    url(r'^answers/(?P<pk>[0-9]+)/$', api.answer_get_edit_delete, name='api-answer-get-edit-delete'),
]