from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from question.models import Question, Answer


@login_required
def list_questions(request):
    questions = Question.objects.annotate(likes=Count('users_like')).order_by('-likes')
    return render(request,
                  'quiz/list_questions.html',
                  {'section': 'quiz',
                   'questions': questions})