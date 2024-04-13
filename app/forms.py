from django import forms

TEXTAREA_ATTRS = {
    "rows": 2,
    "class": "labeled-field"
}

CHOICE_MAX_LENGTH = 150

class QuestionForm(forms.Form):
    title = forms.CharField(
        label="Title",
        required=True,
        widget=forms.TextInput(attrs={"class": "labeled-field"})
    )
    body = forms.CharField(
        label="Body",
        required=False,
        strip=False,
        widget=forms.Textarea(attrs={
            "rows": 3,
            "class": "labeled-field"
        })
    )
    choice1 = forms.CharField(
        label="Choice 1",
        required=True,
        max_length=CHOICE_MAX_LENGTH, 
        widget=forms.Textarea(attrs=TEXTAREA_ATTRS)
    )
    choice2 = forms.CharField(
        label="Choice 2",
        required=True,
        max_length=CHOICE_MAX_LENGTH,
        widget=forms.Textarea(attrs=TEXTAREA_ATTRS)
    )
    choice3 = forms.CharField(
        label="Choice 3",
        required=False,
        max_length=CHOICE_MAX_LENGTH,
        widget=forms.Textarea(attrs=TEXTAREA_ATTRS)
    )
    choice4 = forms.CharField(
        label="Choice 4",
        required=False,
        max_length=CHOICE_MAX_LENGTH,
        widget=forms.Textarea(attrs=TEXTAREA_ATTRS)
    )


class ChoicesForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(ChoicesForm, self).__init__(*args, **kwargs)
        self.fields["choice"] = forms.ChoiceField(
            choices = ((c.id, c.text) for c in question.choices.all()),
            widget = forms.RadioSelect()
        )


class SearchForm(forms.Form):
    search = forms.CharField(label="Seach for a question", required=False)


class AuthForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, required=True)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput())


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="Old Password", required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(label="New Password", required=True, widget=forms.PasswordInput())


class ReportQuestionForm(forms.Form):
    report_question = forms.BooleanField(label="Are you sure you want to report this question?", required=False)


class ContactForm(forms.Form):
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(attrs={
            "rows": 4,
            "class": "labeled-field"
        })
    )

