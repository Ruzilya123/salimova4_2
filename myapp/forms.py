from django import forms

CHOICES = (
    ('novel', 'роман'),
    ('fantasy', 'фантастика')
)

class Form(forms.Form):
    title = forms.CharField(label='название', max_length=250)
    url = forms.CharField(label='ссылка', max_length=250)
    content = forms.CharField(label='содержимое', max_length=250)
    pub = forms.BooleanField(label='публиковать?')
    categories = forms.ChoiceField(label='категория', choices=CHOICES)
    date = forms.DateField(label='дата публикации')

