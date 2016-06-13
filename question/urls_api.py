from django.conf.urls import url

from question import api

urlpatterns = [

    # Questions

    url(r'^questions/$',
        api.question_list_or_post,
        name='api-question-list-or-post'),

    url(r'^questions/(?P<pk>[0-9]+)/$',
        api.question_get_edit_delete,
        name='api-question-get-edit-delete'),

    url(r'^questions/(?P<pk>[0-9]+)/like/$',
        api.question_like,
        name='api-question-like'),

    # Answers

    # url(r'^answers/$',
    #     api.answer_list_or_post,
    #     name='api-answer-list-or-post'),

    url(r'^questions/(?P<pk>[0-9]+)/answer/$',
        api.answer_get_post_edit_delete,
        name='api-answer-get-post-edit-delete'),

    url(r'^questions/(?P<pk>[0-9]+)/answer/like/$',
        api.answer_like,
        name='api-answer-like'),
]
