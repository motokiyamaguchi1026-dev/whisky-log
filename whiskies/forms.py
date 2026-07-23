from django import forms
from .models import Whisky


class WhiskyForm(forms.ModelForm):

    class Meta:
        model = Whisky
        fields = [
            "name",
            "distillery",
            "country",
            "age",
            "abv",
            "memo",
        ]

        labels = {
            "name": "ウイスキー名",
            "distillery": "蒸留所",
            "country": "国",
            "age": "熟成年数",
            "abv": "アルコール度数",
            "memo": "メモ",
        }