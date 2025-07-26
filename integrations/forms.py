from django import forms

class UploadFileForm(forms.Form):
    picture = forms.FileField();
    helper_text = forms.CharField(max_length=120)

    def __str__(self):
        return self.helper_text
    