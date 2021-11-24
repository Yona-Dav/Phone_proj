from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PhoneForm(forms.Form):
    name = forms.CharField(max_length=40, required=False)
    phone_number = PhoneNumberField(max_length=25,required=False,region="IL")

    def clean(self):
        cleaned_data = super(PhoneForm, self).clean()

        name = cleaned_data.get("name")
        phone_number = cleaned_data.get("phone_number")

        if name and phone_number:  # both were entered
            raise forms.ValidationError("Enter only one of name or phone number")
        elif not name and not phone_number:  # neither were entered
            raise forms.ValidationError("You must enter a name or a phone number")

        return cleaned_data
