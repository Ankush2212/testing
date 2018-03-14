from django import forms



# our new form
class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    Last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # content = forms.CharField(
	# required=True,
	# widget=forms.Textarea
	# )
	
