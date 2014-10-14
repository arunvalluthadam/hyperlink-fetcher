from django import forms
from models import HyperlinkField

class HyperlinkForm(forms.ModelForm):

	class Meta:
		model = HyperlinkField
		fields = ('address',)