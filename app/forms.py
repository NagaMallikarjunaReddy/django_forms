from django import forms
g={('male','male'),("female",'female')}
class student(forms.Form):
    Rollno=forms.IntegerField()
    Name=forms.CharField(max_length=100)
    Branch=forms.CharField(max_length=100)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)