from django import forms
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
        
    )
    
    card_number = forms.CharField(
        max_length=19,
        widget=forms.TextInput(attrs={
            'placeholder': '4242 4242 4242 4242',
            'class': 'form-control'
        }),
        label="Card Number",
        
    )
    
    expiry = forms.CharField(
        max_length=7,
        widget=forms.TextInput(attrs={
            'placeholder': 'MM/YYYY',
            'class': 'form-control'
        }),
        label="Expiration Date",
        
    )
    
    cvv = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': '123',
            'class': 'form-control'
        }),
        label="CVV",
        
    )
    
    card_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Name on Card',
            'class': 'form-control'
        }),
        label="Name on Card"
    )
