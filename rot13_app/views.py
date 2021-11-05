from django.shortcuts import render
from django import forms

from rot13_app.utils import RotCipher
# Create your views here.
class RenderForm(forms.Form):
    rotation = forms.IntegerField(max_value=26)
    word = forms.CharField(max_length=75)

def render_index(request):
    return render(request, 'rot13_app/index.html', {'form':RenderForm()})

def result(request):
    form = RenderForm(request.POST)

    if request.method == 'GET':
        return render(request, 'rot13_app/index.html', {'form':RenderForm()})

    elif request.method == 'POST':

        if form.is_valid():
            rotn = form.cleaned_data['rotation']
            user_word = form.cleaned_data['word']
            
            rotation = RotCipher(rotn)
            e_word = rotation.encrypt(user_word)
            d_word = rotation.decrypt(e_word)
    
            return render(request, 'rot13_app/result.html', {'rotation': rotation, 'e_word': e_word, 'd_word': d_word})