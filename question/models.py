from django.db import models
from django.conf import settings


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='question_created_by')
    text = models.CharField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True,
                                      db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='question_liked',
                                        blank=True)

    def get_likes(self):
        return self.users_like.count()

    def __str__(self):
        return self.text[:30] + '...' if len(self.text) > 30 else self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='answer_created_by')
    text = models.CharField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='answer_liked',
                                        blank=True)

    class Meta:
        unique_together = (('question', 'user'), )
        # ordering = ['-created_on']

    def get_likes(self):
        return self.users_like.count()

    def __str__(self):
        return self.text[:30] + '...' if len(self.text) > 30 else self.text
