# from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import Profile
from question.models import Question, Answer
from question.serializers import QuestionSerializer, AnswerSerializer
from quickpoller import permissions as project_permissions


# API part of VIEWS

# -------------------------- QUESTION ----------------------------

@api_view(['GET', 'POST'])
def question_list_or_post(request):
    """List all Questions or create a new one."""
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, project_permissions.IsOwnerOrReadOnly))
def question_get_edit_delete(request, pk):
    """Get, Edit or Delete specific Question if you are an owner."""
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def question_like(request, pk):
    if request.method == 'POST':
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.get(user=request.user)
        if profile not in question.users_like.all():
            question.users_like.add(profile)
        else:
            question.users_like.remove(profile)
        return Response(status=status.HTTP_200_OK)


# -------------------------- ANSWER ------------------------------


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, project_permissions.IsOwnerOrReadOnly))
def answer_get_post_edit_delete(request, pk):
    """Get, Edit or Delete specific Answer if you are an owner."""
    profile = Profile.objects.get(user=request.user)
    try:
        answer = Answer.objects.get(question=pk, user=profile)
    except Answer.DoesNotExist:
        if request.method == 'POST':
            data = request.data
            data['user'] = profile.id
            data['question'] = pk
            serializer = AnswerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def answer_like(request, pk):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        try:
            answer = Answer.objects.get(question=pk, user=profile)
        except Answer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if profile not in answer.users_like.all():
            answer.users_like.add(profile)
        else:
            answer.users_like.remove(profile)
        return Response(status=status.HTTP_200_OK)
