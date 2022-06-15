from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'title ...'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'content ...'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['author']


class CreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'title...'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'content...'
        })

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['author', 'status']