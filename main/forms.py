from django import forms
from main.models import SpeedModel

class SpeedModelForm(forms.ModelForm):
	class Meta:
		model = SpeedModel
		fields = '__all__'


class SpeedModelForm2(forms.Form):
	title = forms.CharField(required=True)
	info = forms.CharField(required=True, widget=forms.Textarea)
	image = forms.ImageField(required=True)

class SpeedModelUpdateForm(forms.Form):
	title = forms.CharField(required=False)
	info = forms.CharField(required=False, widget=forms.Textarea)
	image = forms.ImageField(required=False)