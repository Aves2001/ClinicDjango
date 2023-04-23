from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import Select
from django.utils.translation import gettext_lazy as _

from .models import Visit

user = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = user


class MySelect(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = True
        return option


class VisitForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"type": "text",
                                                         'name': 'name',
                                                         'placeholder': "Ваше ім`я",
                                                         }))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={"type": "text",
                                                                'name': 'name',
                                                                'placeholder': "По-Батькові",
                                                                }))

    class Meta:
        model = Visit
        fields = ['name', 'middle_name', 'specAn', 'nameAnim', 'reason', 'phone', 'textArea']

        widgets = {
            'specAn': MySelect(),
            'nameAnim': forms.TextInput(attrs={
                "type": "text",
                'name': 'nameAnim',
                'placeholder': "Кличка вихованця",
            }),
            'reason': MySelect(),
            'phone': forms.NumberInput(attrs={
                'width': "500px",
                'type': "text",
                'name': "phone",
                'placeholder': "Контактний номер телефону",
            }),
            'textArea': forms.Textarea(attrs={
                'maxlength': "300",
                'name': "textArea",
                'placeholder': "Додаткова інформація",
                'autocomplete': "off",
            }),
        }
