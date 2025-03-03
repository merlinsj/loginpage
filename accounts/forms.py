from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role', 'security_code']

    def clean_security_code(self):
        role = self.cleaned_data.get('role')
        security_code = self.cleaned_data.get('security_code')

        # Define valid security codes for each role
        valid_security_codes = {
            'student': 'student123',  # Replace with actual code for students
            'teacher': 'teacher123',  # Replace with actual code for teachers
            'admin': 'admin123',  # Optional, Admin validation handled by superuser
        }

        if role in valid_security_codes:
            if security_code != valid_security_codes[role]:
                raise forms.ValidationError(f"Invalid security code for {role}s.")

        return security_code
