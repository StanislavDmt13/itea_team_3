from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import QuestionForm
from db.models import Question

@login_required
def my_questions(request):
    question = Question.objects.filter(user=request.user).order_by('-date_create')
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        field_errors = [(field.label, field.errors) for field in form]
        print(field_errors)
        if form.is_valid():
            print(form)
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('support'))
    return render(request, 'support.html', {'question': question})


class SupportView(TemplateView):
    template_name = 'support.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(**kwargs)

