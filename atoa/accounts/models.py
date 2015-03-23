from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, limit_choices_to={'is_active': True})
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def is_answered(self, user):
        try:
            self.answer_set.get(answered_by=user)
            # Answer.objects.get(question=self, answered_by=user)
            return True
        except Answer.DoesNotExist:
            return False


class Answer(models.Model):
    answered_by = models.ForeignKey(User,
        limit_choices_to={'is_active': True})
    question = models.ForeignKey(Question, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content[:20]