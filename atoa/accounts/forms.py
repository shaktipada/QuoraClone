from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django import forms

from accounts.models import Question, Answer

class AccountRegistration(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        help_texts = {'username': "", }
        widgets = {'password': forms.PasswordInput(), }

    def clean(self):
        cleaned_data = super(AccountRegistration, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if confirm_password != password:
            raise forms.ValidationError("Password confirmation failed")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("Already an user at A2A")

        except User.DoesNotExist:
            return email

    def save(self):
        cleaned_data = self.cleaned_data
        user = User.objects.create_user(
            cleaned_data['username'],
            email=cleaned_data['email'],
            password=cleaned_data['password'])
        return user

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserLogin, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError("invalid Username or Password")

            if not user.is_active:
                raise forms.ValidationError("Inactive User. Please register")

            cleaned_data['user'] = user
            return cleaned_data

class QuestionPost(ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'content')

    def clean(self):
        cleaned_data = super(QuestionPost, self).clean()
        return cleaned_data

    def save(self, user):
        instance = super(QuestionPost, self).save(commit=False)
        instance.user = user
        instance.save()
        return instance


class AnswerPost(ModelForm):

    class Meta:
        model = Answer
        fields = ('content', )

    def clean(self):
        cleaned_data = super(AnswerPost, self).clean()
        return cleaned_data

    def save(self, user=None, question=None):
        if not user and not question:
            return super(AnswerPost, self).save()
        instance = super(AnswerPost, self).save(commit=False)
        instance.answered_by = user
        instance.question = question
        instance.save()
        return instance