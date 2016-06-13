from django.conf.urls import url

from question import views

urlpatterns = [

    url(r'^$', views.list_questions, name='list_questions'),
    # url(r'^$', views.list_questions, name='questions'),
    # url(r'^questions/$', views.question_list_or_post, name='question-list-or-post'),
    # url(r'^questions/(?P<pk>[0-9]+)/$', views.question_get_edit_delete, name='question-get-edit-delete'),

]