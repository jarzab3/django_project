from django import forms
from django.shortcuts import render
from django.http import Http404

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder, HTML, Div, Row
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions, AppendedText)

from regression.models import UserStory

class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = [
            "subject",
            "case_title",
            "repro_steps",
            "test_preconditions",
            "extra_notes"
        ]

    case_title = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    test_preconditions = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)
    repro_steps = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    extra_notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(

            Div(
                Field('subject'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('case_title'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('test_preconditions'), css_class="col-md-6 col-md-offset-3"
            ),
            Div(
                Field('repro_steps'), css_class="col-md-6 col-md-offset-3",
                      # style="background: #FAFAFA; "
            ),
            Div(
                Field('extra_notes'), css_class="col-md-6 col-md-offset-3"
            ),

            Div(
                Submit('submit', "Save"), css_class="col-md-6 col-md-offset-3"
            )
        )

#
# class LoginForm(forms.Form):
#    user = forms.CharField(max_length = 100)
#    password = forms.CharField(widget = forms.PasswordInput())
