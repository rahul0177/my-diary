from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model=Entry
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control','placeholder':"what's on your mind"})