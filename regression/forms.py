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

    repro_steps = forms.CharField(widget=forms.Textarea)
    test_preconditions = forms.CharField(widget=forms.Textarea)
    extra_notes = forms.CharField(widget=forms.Textarea)

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


class MessageForm(forms.Form):
    text_input = forms.CharField()

    textarea = forms.CharField(
        widget=forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', 'Option two can also be checked and included in form results'),
            (
                'option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text="Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('text_input', css_class='input-xlarge'),
        Field('textarea', rows="3", css_class='input-xlarge'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

#
# class LoginForm(forms.Form):
#    user = forms.CharField(max_length = 100)
#    password = forms.CharField(widget = forms.PasswordInput())
