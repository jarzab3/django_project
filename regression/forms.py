from django import forms
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder, HTML, Div, Row
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions, AppendedText)

from regression.models import UserStory
from regression.models import Category


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description"
        ]

    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 15}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Div(
                Field('name'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('description'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Submit('submit', "Save"), css_class="col-md-6 col-md-offset-3"
            )
        )


class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = [
            "category",
            "subject",
            "domain",
            "case_title",
            "repro_steps",
            "test_preconditions",
            "extra_notes"
        ]

    case_title = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    repro_steps = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    test_preconditions = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)
    extra_notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Div(
                Field('category'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('subject'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('domain'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('case_title'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('repro_steps'), css_class="col-md-6 col-md-offset-3",
                # style="background: #FAFAFA; "
            ),
            Div(
                Field('test_preconditions'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('extra_notes'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Submit('submit', "Save"), css_class="col-md-6 col-md-offset-3"
            )
        )
