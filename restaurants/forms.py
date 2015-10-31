from django import forms

class CommentForm (forms.Form):
	user = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=50, required=False)
	content = forms.CharField(max_length=200, widget=forms.Textarea)

	def clean_content(self):
		content = self.cleaned_data['content']
		if len(content)<2:
			raise forms.ValidationError('字數不足')
		return content
		
