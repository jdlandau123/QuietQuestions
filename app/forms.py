from django import forms

class QuestionForm(forms.Form):
    text = forms.CharField(label="Question Text", required=True, widget=forms.Textarea(attrs={
        "rows": 3,
        "class": "labeled-field"
    }))
    choice1 = forms.CharField(label="Choice 1", required=True, widget=forms.Textarea(attrs={
        "rows": 2,
        "class": "labeled-field"
    }))
    choice2 = forms.CharField(label="Choice 2", required=True, widget=forms.Textarea(attrs={
        "rows": 2,
        "class": "labeled-field"
    }))
    choice3 = forms.CharField(label="Choice 3", required=False, widget=forms.Textarea(attrs={
        "rows": 2,
        "class": "labeled-field"
    }))
    choice4 = forms.CharField(label="Choice 4", required=False, widget=forms.Textarea(attrs={
        "rows": 2,
        "class": "labeled-field"
    }))


class ChoicesForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(ChoicesForm, self).__init__(*args, **kwargs)
        self.fields["choice"] = forms.ChoiceField(
            choices = ((c.id, c.text) for c in question.choices.all()),
            widget = forms.RadioSelect()
        )


