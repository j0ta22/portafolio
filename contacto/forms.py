from django import forms


class Contacto(forms.Form):
    
    nombre = forms.CharField(label="nombre", required=True, max_length=100,widget=forms.TextInput(attrs={'size': '38'}))
    
    email = forms.EmailField(label="email", required=True, max_length=100, widget=forms.TextInput(attrs={'size': '38'}))
    
    contenido = forms.CharField(label="contenido", widget=forms.Textarea)