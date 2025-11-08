from django.db import models
from django.contrib.auth.models import User

class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.CharField(max_length=255)
    definition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcards = models.ManyToManyField(Flashcard)
    created_at = models.DateTimeField(auto_now_add=True)

class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
