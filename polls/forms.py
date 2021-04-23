# this file is created manually, not a built in

from django import forms

class CreateNewList(forms.Form):
    # setting 'required=False' will not show the note
    name = forms.CharField(label="name", max_length=200)
    check = forms.BooleanField(required=False)