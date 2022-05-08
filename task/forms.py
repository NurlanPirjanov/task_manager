from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class AddForm(forms.ModelForm):
    class Meta:
        model = TaskManager
        fields = ('title', 'file', 'active','do_date', 'role_user', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'shadow-sm my-2 max-w-xl  block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-white text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'do_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'shadow-sm my-2 max-w-sm bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'file': forms.FileInput(attrs={'class': 'my-2 shadow-sm max-w-sm flex w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-white dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),
            'active': forms.CheckboxInput(attrs={ 'class': 'my-2 w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600', 'role': 'switch',}),
            'role_user': forms.Select(attrs={'class': 'my-2 max-w-sm bg-white shadow-sm border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'body': forms.CharField(widget=CKEditorWidget()),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'file',)