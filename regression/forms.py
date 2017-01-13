from django import forms
from django.shortcuts import render
from django.http import Http404

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder, HTML, Div
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from regression.models import UserStory



class PostForm(forms.ModelForm):
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
        #self.helper.form_show_labels = False

        # self.helper.layout = Layout(
        #     Field('subject', css_class="col-md-4")
        #     )
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

        # self.helper.layout.append(
        #     HTML('<button type="submit" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">')  
        #     )
   # <!-- <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Open Modal</button> -->


'''

class PostForm(forms.ModelForm):
    class Meta:
        model = user_story
        fields = [
            "subject",
            "case_title",
            "repro_steps",
            "test_preconditions",
            "extra_notes"
        ]


    def __init__(self, *args, **kwargs):
       super(PostForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper(self)
       self.helper.form_class = 'form-horizontal'
       self.helper.layout.append( 
        Fieldset(
        'Tell us your favorite stuff {{ username }}',
        'like_website',
           FormActions(
               Submit('save_changes', 'Save', css_class='btn-primary'),
               #Submit('cancel', 'Cancel'),
           )
           )
       )

    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Fieldset(
    #             'first arg is the legend of the fieldset',
    #             'like_website',
    #             'favorite_number',
    #             'favorite_color',
    #             'favorite_food',
    #             'notes'
    #         ),
    #         ButtonHolder(
    #             Submit('submit', 'Submit', css_class='button white')
    #         )
    #     )
    '''