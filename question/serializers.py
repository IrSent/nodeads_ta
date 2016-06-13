from rest_framework import serializers
from question.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializing all the Questions
    """
    class Meta:
        model = Question
        fields = ('id', 'text', 'users_like')

class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializing all the Answers
    """
    class Meta:
        model = Answer
        fields = ('id', 'question', 'text', 'users_like')