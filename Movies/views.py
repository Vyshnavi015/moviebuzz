from django.shortcuts import render

# Create your views here.
from .models import Buzz, Question

def movie_quiz(request):
    if request.method == "POST":
        # Get user input from the form
        user_input_language = request.POST.get('language')
        user_input_actor = request.POST.get('actor')

        # Fetch matching movies
        matching_movies = Buzz.objects.filter(language=user_input_language, actor=user_input_actor)

        if matching_movies.exists():
            # Fetch related questions
            quiz_questions = Question.objects.filter(movie__in=matching_movies)
            return render(request, 'quiz.html', {'questions': quiz_questions})
        else:
            return render(request, 'quiz.html', {'error': "No movies found matching your criteria."})
    
    return render(request, 'quiz.html')
