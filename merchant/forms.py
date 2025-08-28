from django import forms
from accounts.models import CustomUser
from .models import MerchantProfile


from django import forms

class MerchantLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )

class MerchantSignupForm(forms.ModelForm):
    # User fields
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    # MerchantProfile fields
    company_name = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=50)
    business_address = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.URLField(required=False)
    contact_person_name = forms.CharField(max_length=100, required=False)
    contact_phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "full_name",
            "phone_number",
            "password1",
            "password2",
            "company_name",
            "license_number",
            "business_address",
            "website",
            "contact_person_name",
            "contact_phone",
        )

    def clean_password2(self):
        pw1 = self.cleaned_data.get("password1")
        pw2 = self.cleaned_data.get("password2")
        if pw1 != pw2:
            raise forms.ValidationError("Passwords do not match")
        return pw2

    def save(self, commit=True):
        # Create user
        user = CustomUser(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            full_name=self.cleaned_data["full_name"],
            phone_number=self.cleaned_data["phone_number"],
            role="merchant",
        )
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

            # Create MerchantProfile
            MerchantProfile.objects.create(
                user=user,
                company_name=self.cleaned_data["company_name"],
                license_number=self.cleaned_data["license_number"],
                business_address=self.cleaned_data.get("business_address"),
                website=self.cleaned_data.get("website"),
                contact_person_name=self.cleaned_data.get("contact_person_name"),
                contact_phone=self.cleaned_data.get("contact_phone"),
            )
        return user
