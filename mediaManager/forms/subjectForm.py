from django import forms
from django.core.exceptions import ValidationError
from mediaManager.creds import db
class SubjectForm(forms.Form):
    subjectName = forms.CharField(label="", widget = forms.TextInput(
        attrs = {
            'class': "w-full bg-gray-800 rounded border border-gray-700 text-white focus:outline-none focus:border-indigo-500 text-base px-4 py-2",
            'placeholder': "Subject Name"
        }
    ),required = True, max_length = 50)
    subjectCode = forms.CharField(label="", widget = forms.TextInput(
        attrs = {
            'class': "w-full bg-gray-800 rounded border border-gray-700 text-white focus:outline-none focus:border-indigo-500 text-base px-4 py-2",
            'placeholder': "Subject Code"
        }
    ),required = True, max_length = 50)
    subjectDescription = forms.CharField(label="", widget = forms.Textarea(
        attrs = {
            'class': "w-full bg-gray-800 rounded border border-gray-700 text-white focus:outline-none h-48 focus:border-indigo-500 text-base px-4 py-2 resize-none block",
            'placeholder' : 'Desription',
            'rows': 5
        }
    ),max_length=500)
    files = forms.FileField(label="", widget=forms.FileInput(
        attrs = {
            'class': "text-base px-4 py-2"
        }
    ),required = True)

    #CUSTOM VALIDATOR
    # def validate_collection(subjectCode):
    #     data = self.cleaned_data["subjectCode"]
    #     if data in db.list_collection_names():
    #         return data
    #     raise ValidationError("This Course is already present") 