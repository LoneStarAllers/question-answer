from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from question.models import Question, Category
from django.urls import reverse

def index(request):
    return render(request, 'question/index.html')

def all_questions(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    context = { 'questions': questions, 'categories':categories}
    return render(request, 'question/all_questions.html', context)

def question_detail(request, id):
    question = Question.objects.get(id=id)
    answers = question.answers.all()
    total_likes = question.total_likes()
    categories = Category.objects.all()
    context = { 'question': question, 'categories':categories, 'answers':answers, 'total_likes':total_likes}
    return render(request, 'question/question_detail.html', context)

def category_questions(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    questions = category.questions.all()
    context = {'categories':categories, 'category':category, 'questions': questions}
    return render(request, 'question/category_questions.html', context)

def likeQuestion(request, pk):
    question = get_object_or_404(Question, id=request.POST.get('question_id'))
    question.likes.add(request.user)
    return HttpResponseRedirect(reverse('question:question_detail', args=[str(pk)]))