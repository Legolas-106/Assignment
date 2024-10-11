from django import forms

APPCHOICES = [('E-commerce','E-commerce'),('Social Media','Social Media'),('Cloud Kitchen','Cloud Kitchen')]

class AppForm(forms.Form):
    # category = forms.ChoiceField(choices=APPCHOICES,required=True,label='App Category')
    # features = forms.MultipleChoiceField(choices=[('','Please select a category')],required=True,label="App Features",widget=forms.CheckboxSelectMultiple)
    input1 = forms.ChoiceField(choices=APPCHOICES)
    input2 = forms.CharField()