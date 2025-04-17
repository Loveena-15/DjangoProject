# qala/forms.py

from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    inquiry_type = forms.ChoiceField(choices=[
        ('general', 'General Inquiry'),
        ('artist', 'Artist Collaboration'),
        ('exhibition', 'Exhibition Information'),
        ('feedback', 'Feedback'),
        ('other', 'Other'),
    ])
    message = forms.CharField(widget=forms.Textarea)

class CheckoutForm(forms.Form):
    # Shipping Information
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'John Doe',
            'class': 'form-control'
        }),
        label="Full Name"
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'john@example.com',
            'class': 'form-control'
        }),
        label="Email Address"
    )
    
    address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': '123 Main St',
            'class': 'form-control'
        }),
        label="Street Address"
    )
    
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'New York',
            'class': 'form-control'
        }),
        label="City"
    )
    
    zip_code = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '10001',
            'class': 'form-control'
        }),
        label="ZIP/Postal Code",
        validators=[
            RegexValidator(
                regex=r'^\d{5}(?:[-\s]\d{4})?$',
                message='Enter a valid ZIP code (e.g., 12345 or 12345-6789)'
            )
        ]
    )
    
    country = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'United States',
            'class': 'form-control'
        }),
        label="Country"
    )
    
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'NY',
            'class': 'form-control'
        }),
        label="State/Province"
    )
    
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '+1 (555) 123-4567',
            'class': 'form-control'
        }),
        label="Phone Number",
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    
    # Payment Method
    card_number = forms.CharField(
        max_length=19,
        widget=forms.TextInput(attrs={
            'placeholder': '4242 4242 4242 4242',
            'class': 'form-control'
        }),
        label="Card Number",
        validators=[
            RegexValidator(
                regex=r'^\d{4}\s?\d{4}\s?\d{4}\s?\d{4}$',
                message='Enter a valid 16-digit card number'
            )
        ]
    )
    
    expiry = forms.CharField(
        max_length=7,
        widget=forms.TextInput(attrs={
            'placeholder': 'MM/YYYY',
            'class': 'form-control'
        }),
        label="Expiration Date",
        validators=[
            RegexValidator(
                regex=r'^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$',
                message='Enter a valid expiration date in MM/YY or MM/YYYY format'
            )
        ]
    )
    
    cvv = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': '123',
            'class': 'form-control'
        }),
        label="CVV",
        validators=[
            RegexValidator(
                regex=r'^\d{3,4}$',
                message='Enter a valid 3 or 4-digit CVV'
            )
        ]
    )
    
    card_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Name on Card',
            'class': 'form-control'
        }),
        label="Name on Card"
    )
