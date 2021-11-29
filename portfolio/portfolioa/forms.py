from django import forms

class aqbw(forms.Form):
    bw1 = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw2 = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw3 = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    anm = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))

class bewertungn(forms.Form):
    bw1Formulierung = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw1Css = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw1Aufbau = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw1Aenderung = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))
    bw2Fancy = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw2Projects = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw2Aenderung = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))
    bw3Dtl = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw3Inhalt = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw3Aenderung = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))
    bw4Bewe = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw4Aenderung = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))
    bw5Start = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw5Proj = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw5Farbe = forms.IntegerField(max_value=10, widget=forms.TextInput(attrs={'type':'range', 'min':'1', 'max':'10'}))
    bw5Aenderung = forms.CharField(widget=forms.TextInput(attrs={'class':'white-text'}))