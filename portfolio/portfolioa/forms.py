from django import forms

class aqbw(forms.Form):
    bw1 = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw2 = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw3 = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    anm = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))