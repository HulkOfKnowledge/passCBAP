from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    name = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_id = models.IntegerField()
    question = models.TextField()
    options = models.JSONField()
    selected_answer = models.CharField(max_length=255, blank=True, null=True)
    correct_answer = models.CharField(max_length=100)
    explanation = models.TextField()

    def __str__(self):
        return self.question


class UserExam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed = models.BooleanField(default=False)
    date_completed = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.exam.name}"