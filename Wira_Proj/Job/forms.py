from django import forms
class SearchForm(forms.Form):
    title= forms.CharField(max_length=30,label="title")
    location = forms.CharField(max_length=30,label="Location")
    experience = forms.CharField(max_length=30,label="Experience")

    class Meta:
        fields=['title','location','experience']

class JobCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea ,label="Job_Description")
    location = forms.CharField(label="Location",widget=forms.Select(choices='Job_Location'))
    salary = forms.DecimalField(label="salary")
    industry = forms.CharField(label="Industry", widget = forms.Select(choices='Job_industry'))

def clean(self):
    cleaned_data = super(SearchForm,self).clean()
    title = cleaned_data.get('title')
    if not title :
        raise forms.ValidationError('Type a keyword')
    return     