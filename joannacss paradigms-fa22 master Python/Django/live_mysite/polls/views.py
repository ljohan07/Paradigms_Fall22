from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Choice, Question



# Feature 1: displays the latest 5 questions
class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")




# Feature 2: displays results for a particular question.
class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"


# Feature 3: displays a question text, with no results but with a form to vote.
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

# Feature 4: handles voting for a particular choice in a particular question.
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



# OLD CODE, from first live demo (simple Hello World!)
# def index(request):
#   context = {'course': "CSE-30332",'semester':'Fall 22'}
#   return render(request, 'polls/index.html', context)
