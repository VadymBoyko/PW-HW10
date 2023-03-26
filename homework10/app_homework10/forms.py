from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, Textarea

from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(max_length=150, required=True, widget=TextInput(attrs={"class": "form-control"}))
    birthday = CharField(max_length=50, required=True, widget=TextInput(attrs={"class": "form-control"}))
    birth_place = CharField(max_length=150, required=True, widget=TextInput(attrs={"class": "form-control"}))
    bio = CharField(max_length=15000, required=True, widget=Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ['fullname', 'birthday', 'birth_place', 'bio']


class QuoteForm(ModelForm):
    quote = CharField(max_length=250, required=True, widget=TextInput(attrs={"class": "form-control"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), required=True, empty_label=None)

    class Meta:
        model = Quote
        fields = ['quote', 'author']
