from django import forms
from django.shortcuts import render
from django.http import Http404

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder, HTML, Div
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from regression.models import UserStory



class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields =[
            "subject",
            "case_title",
            "repro_steps",
            "test_preconditions",
            "extra_notes"
            ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Div(
                Field('subject'), css_class="col-md-6 col-md-offset-3"
                ),
            Div(
                Field('case_title'), css_class="col-md-6 col-md-offset-3"
                ),
            Div(
                Field('repro_steps'), css_class="col-md-6 col-md-offset-3"
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
