from django import forms
from apis.models import Task


# Create the form class.
class MakeForm(forms.ModelForm):
    class Meta:
        model = Task  # Specify the model that the form is based on
        fields = ['status', 'title', 'description']  # Define the fields from the model to include in the form
