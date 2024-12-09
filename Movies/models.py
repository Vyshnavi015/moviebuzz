from django.db import models

class Buzz(models.Model):
    language = models.CharField(max_length=20)
    actor = models.CharField(max_length=20)
    movie = models.CharField(max_length=20)

    def __str__(self):
        return self.movie  # Display the movie name when using Buzz instances


class Question(models.Model):
    movie = models.ForeignKey(Buzz, on_delete=models.CASCADE)  # Use Buzz instead of Movie
    question_text = models.TextField()
    options = models.JSONField()  # Store a list of options
    correct_option = models.IntegerField()  # Store the index of the correct option

    def __str__(self):
        return self.question_text  # Display the question text for debugging or in admin

    
