from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['term', 'definition']
        widgets = {
            'term': forms.TextInput(attrs={'class': 'form-control'}),
            'definition': forms.Textarea(attrs={'class': 'form-control'}),
        }
