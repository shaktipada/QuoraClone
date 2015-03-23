from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import *
from accounts.models import Question, Answer

def accountRegistration_view(request):

    if request.method == 'POST':
        form = AccountRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login_page'))

    else:
        form = AccountRegistration()

    return render(request, 'accounts/registeration.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        form = UserLogin(request.POST)

        if form.is_valid():
            login(request, form.cleaned_data['user'])
            return redirect(reverse("home_page"))
        else:
            print form.errors

    else:
        form = UserLogin()

    return render(request, 'accounts/login.html', {"form": form})


@login_required(login_url='/accounts/login/')
def home_view(request):
    return render(request, 'accounts/home.html', {})


@login_required(login_url='/accounts/login/')
def questions_view(request):

    posts = Question.objects.all()

    return render(request, 'accounts/questions.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
def question_view(request, id):

    current_user = request.user
    post_q = Question.objects.get(id=id)
    post_a = Answer.objects.filter(question=post_q)
    my_a = Answer.objects.filter(answered_by=current_user)
    current_user_answered = post_q.is_answered(current_user)

    if request.method == 'POST':
        form = AnswerPost(request.POST)

        if form.is_valid():
            form.save(current_user, post_q)
            return redirect(reverse("questions_page"))
        else:
            print form.errors

    else:
        form = AnswerPost()

    return render(request, 'accounts/answer.html',
        {   'form': form,
            'post_q': post_q, 'post_a': post_a,
            'current_user_answered': current_user_answered,
            'my_a': my_a
        })



@login_required(login_url='/accounts/login/')
def edit_view(request, id):
    edit_answer = Answer.objects.get(id=id)

    form = AnswerPost(instance=edit_answer)
    if request.method == "POST":
        form = AnswerPost(request.POST, instance=edit_answer)
        if form.is_valid():
            form.save()
            return redirect(reverse("question_page", args=[edit_answer.question.id]))

    return render(request, 'accounts/edit.html', {'form': form})


@login_required(login_url='/accounts/login/')
def my_questions_view(request):
    current_user = request.user
    my_posts = Question.objects.filter(user_id=current_user.id)

    if request.method == 'POST':
        form = QuestionPost(request.POST)

        if form.is_valid():
            form.save(current_user)
            return redirect(reverse("questions_page"))
        else:
            print form.errors

    else:
        form = QuestionPost()

    return render(request, 'accounts/myquestions.html',
        {'form': form, 'my_posts': my_posts})


@login_required(login_url='/accounts/login/')
def delete_q_view(request, id):

    del_q = Question.objects.get(id=id)

    if request.method == 'POST':
        del_q.delete()

    return redirect(reverse('questions_page'))


@login_required(login_url='/accounts/login/')
def delete_a_view(request, id):

    del_a = Answers.objects.get(id=id)

    if request.method == 'POST':
        del_a.delete()

    return redirect('accounts/answer.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('login_page'))