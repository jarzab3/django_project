from django import forms
from django.shortcuts import render
from django.http import Http404


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class SimpleForm(forms.Form):
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember Me?")

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'login', css_class='btn-primary'))

class CartForm(forms.Form):
    item = forms.CharField()
    quantity = forms.IntegerField(label="Qty")
    price = forms.DecimalField()

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        'item',
        PrependedText('quantity', '#'),
        PrependedAppendedText('price', '$', '.00'),
        FormActions(Submit('login', 'login', css_class='btn-primary'))
    )


class AddNewUserStory(forms.Form):
    subject_f = forms.CharField(label="Subject", required=True)
    case_title_f = forms.CharField(label="Case Title", required=True, max_length=56)
    test_preconditions_f = forms.DateField(label="Test Preconditions") #input_formats=['%m/%y'])
    repro_steps_f = forms.IntegerField(label="Repro Steps", required=True)
    notes_f = forms.CharField(label="Extra Notes", widget=forms.Textarea())

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('subject_f', css_class='input-sm'),
        Field('case_title_f', css_class='input-sm'),
        Field('test_preconditions_f', css_class='input-sm'),
        Field('repro_steps_f', css_class='input-sm'),
        Field('notes_f', rows=3),
        FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
    )

#def forms(request):
#    return render(request, "regression/forms.html", {'form': AddNewUserStory()})

'''
from regression.models import user_story

class PostForm(forms.Form):
    #content = forms.CharField(max_length=256)
    #created_at = forms.DateTimeField()
    pass
 

class USForm(forms.Form):
    pass


def post_form_upload(request):
    if request.method == 'GET':
        #form = PostForm()

        # A POST request: Handle Form Upload
        form = USForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            #post = m.Post.objects.create(content=content,
             #                            created_at=created_at)
            user_story_object = user_story(title=content, description=created_at)
            user_story_object.save()    
            #return HttpResponseRedirect(reverse('post_detail',
            #                                    kwargs={'post_id': post.id}))
            
            return HttpResponseRedirect(reverse('regression:user_story'))
        else:
            form - USForm()



    return render(request, 'regression/forms.html', {
        'form': form,
    })




'''

class CostForm(forms.Form):
    fields = forms.CharField(max_length=256)



from regression.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title"
,           "content"
        ]