from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PhoneForm(forms.Form):
    name = forms.CharField(max_length=40, required=False)
    phone_number = PhoneNumberField(max_length=25,required=False,region="IL")
    email = forms.CharField(max_length=100, required=False)

    def clean(self):
        cleaned_data = super(PhoneForm, self).clean()

        name = cleaned_data.get("name")
        phone_number = cleaned_data.get("phone_number")
        email = cleaned_data.get("email")

        if (name and phone_number) or (name and email) or (phone_number and email):  # both were entered
            raise forms.ValidationError("Fill only one field")
        elif not name and not phone_number and not email:  # neither were entered
            raise forms.ValidationError("You must enter a name or a phone number or an email")

        return cleaned_data
