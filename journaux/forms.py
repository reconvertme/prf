from django import forms
from journaux.models import Journal

# La classe Form
class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

# Formulaire à partir d'un modèle
class JournalForm(forms.ModelForm):
   class Meta:
     model = Journal
     fields = '__all__'