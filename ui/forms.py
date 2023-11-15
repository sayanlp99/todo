from django import forms
from base.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']
        # You can customize widgets and labels if needed
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Enter description'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
        }
