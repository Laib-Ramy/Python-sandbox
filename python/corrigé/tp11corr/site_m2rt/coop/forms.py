from django import forms

class AddToolForm(forms.Form):
    description = forms.CharField(max_length=256, label="Description")
    price=forms.DecimalField(decimal_places=2, max_digits=6, label="Prix")

