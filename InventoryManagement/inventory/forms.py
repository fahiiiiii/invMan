# from django import forms
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.contrib.gis.geos import GEOSGeometry
# from django.contrib.gis.forms import PointField
# from django.core.validators import MinValueValidator, MaxValueValidator
# from models import Accommodation, Location
# from django.contrib.gis.forms import PointField
# from django.contrib.gis.geos import Point
# # # class AccommodationForm(forms.ModelForm):
# # #     # Add an additional constructor to accept the request object
# # #     def __init__(self, *args, **kwargs):
# # #         self.request = kwargs.pop('request', None)  # Accept the request object
# # #         super().__init__(*args, **kwargs)

# # #     class Meta:
# # #         model = Accommodation
# # #         fields = ['id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'images', 'location', 'amenities']
# # #         exclude = ['id']
# # #     def save(self, commit=True):
# # #         accommodation = super().save(commit=False)
# # #         if commit and self.request:
# # #             accommodation.user = self.request.user  # Set the user to the currently logged-in user
# # #             accommodation.save()
# # #         return accommodation




# # # class AccommodationForm(forms.ModelForm):
# # #     def __init__(self, *args, **kwargs):
# # #         self.request = kwargs.pop('request', None)  # Accept the request object
# # #         super().__init__(*args, **kwargs)

# # #     class Meta:
# # #         model = Accommodation
# # #         # fields = ['id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'images', 'location', 'amenities']
# # #         # exclude = ['id']
# # #         fields = ['title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'images', 'location', 'amenities']
# # #     def save(self, commit=True):
# # #         accommodation = super().save(commit=False)
# # #         if commit and self.request:
# # #             accommodation.user = self.request.user  # Set the user to the currently logged-in user
# # #             accommodation.save()
# # #         return accommodation

# # # class AccommodationForm(forms.ModelForm):
# # #     def __init__(self, *args, **kwargs):
# # #         self.request = kwargs.pop('request', None)  # Accept the request object
# # #         super().__init__(*args, **kwargs)

# # #     class Meta:
# # #         model = Accommodation
# # #         fields = ['title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'images', 'location', 'amenities']

# # #     # Clean amenities to ensure it's a valid JSON (empty list if no input)
# # #     def clean_amenities(self):
# # #         amenities = self.cleaned_data.get('amenities')
# # #         if not amenities:
# # #             return []  # Ensure it's an empty list if no amenities are selected
# # #         return amenities

# # #     def save(self, commit=True):
# # #         accommodation = super().save(commit=False)
# # #         if commit and self.request:
# # #             accommodation.user = self.request.user  # Set the user to the currently logged-in user
# # #             accommodation.save()
# # #         return accommodation

# # from django import forms
# # from .models import Property
# # from django.contrib.auth.models import User
# # from django.forms import ClearableFileInput

# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = ['id', 'feed', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'images', 'location', 'amenities', 'published']

#     images = forms.ImageField(widget=ClearableFileInput(attrs={'multiple': True}), required=False)



# # class AccommodationForm(forms.ModelForm):
# #     center = PointField(widget=forms.TextInput(attrs={'placeholder': 'POINT(longitude latitude)'}))
# #     # File upload field for multiple images
# #     images = forms.FileField(
# #     widget=forms.ClearableFileInput(attrs={'multiple': True}),
# #     required=False,
# #     help_text="Upload multiple property images."
# # )


# #     # Choices for countries
# #     COUNTRY_CHOICES = [
# #         ('US', 'United States'),
# #         ('CA', 'Canada'),
# #         ('LA', 'Laos'),
# #         # Add more countries as needed
# #     ]

# #     # Choices for amenities
# #     AMENITIES_CHOICES = [
# #         ('parking', 'Parking'),
# #         ('wifi', 'WiFi'),
# #         ('pool', 'Swimming Pool'),
# #         ('gym', 'Gym'),
# #         ('kitchen', 'Kitchen'),
# #         # Add more amenities
# #     ]

# #     # Override some fields with more specific widgets and validators
# #     title = forms.CharField(
# #         max_length=200,
# #         widget=forms.TextInput(attrs={'class': 'form-control'}),
# #         help_text="Enter a descriptive title for the property"
# #     )

# #     country_code = forms.ChoiceField(
# #         choices=COUNTRY_CHOICES,
# #         widget=forms.Select(attrs={'class': 'form-control'}),
# #         help_text="Select the country code"
# #     )

# #     country = forms.CharField(
# #         max_length=100,
# #         widget=forms.TextInput(attrs={'class': 'form-control'}),
# #         help_text="Full country name"
# #     )

# #     bedroom_count = forms.IntegerField(
# #         validators=[MinValueValidator(1), MaxValueValidator(20)],
# #         widget=forms.NumberInput(attrs={'class': 'form-control'}),
# #         help_text="Number of bedrooms (1-20)"
# #     )

# #     review_score = forms.FloatField(
# #         validators=[MinValueValidator(0), MaxValueValidator(5)],
# #         widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
# #         help_text="Review score (0-5)"
# #     )

# #     usd_rate = forms.DecimalField(
# #         max_digits=10, 
# #         decimal_places=2,
# #         validators=[MinValueValidator(0)],
# #         widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
# #         help_text="Price in USD"
# #     )

# #     center = PointField(
# #         widget=forms.TextInput(attrs={'class': 'form-control'}),
# #         help_text="Enter location coordinates (longitude, latitude)"
# #     )

# #     published = forms.BooleanField(
# #         required=False,
# #         widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
# #         help_text="Make this property visible"
# #     )

# #     amenities = forms.MultipleChoiceField(
# #         choices=AMENITIES_CHOICES,
# #         widget=forms.CheckboxSelectMultiple,
# #         required=False,
# #         help_text="Select available amenities"
# #     )

# #     class Meta:
# #         model = Accommodation
# #         fields = [
# #             'title', 'country_code', 'country', 'bedroom_count', 
# #             'review_score', 'usd_rate', 'center', 'published', 
# #             'amenities'
# #         ]

# #     def clean_images(self):
# #         images = self.cleaned_data.get('images')
        
# #         if images:
# #             # Ensure it's an InMemoryUploadedFile (image upload)
# #             if isinstance(images, InMemoryUploadedFile):
# #                 max_upload_size = 5 * 1024 * 1024  # 5MB max upload size
# #                 if images.size > max_upload_size:
# #                     raise ValidationError("Image size exceeds the 5MB limit.")
# #             else:
# #                 raise ValidationError("Invalid image file.")
# #         return images

# #     def clean_center(self):
# #         center = self.cleaned_data.get('center')
# #         try:
# #             # Validate that it's a valid WKT point
# #             point = GEOSGeometry(center)
# #             if point.geom_type != 'Point':
# #                 raise ValidationError("Invalid geometry type. Please provide a POINT.")
# #         except Exception:
# #             raise ValidationError("Invalid geometry value. Please provide a valid POINT(longitude latitude).")
# #         return center

# class PropertyOwnerSignUpForm(forms.ModelForm):
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(), 
#         label="Password", 
#         min_length=8,  # You can specify a minimum length for the password if needed
#         required=True
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(), 
#         label="Confirm Password", 
#         required=True
#     )
#     phone = forms.CharField(
#         max_length=15,
#         label="Phone Number",
#         required=True
#     )
#     location = forms.CharField(
#         max_length=100,
#         label="Location",
#         required=True
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean_password2(self):
#         """
#         Check that the password1 and password2 fields match.
#         """
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords do not match.")
#         return password2

#     def clean_phone(self):
#         """
#         Ensure the phone number is numeric.
#         """
#         phone = self.cleaned_data.get("phone")
#         if not phone.isdigit():
#             raise ValidationError("Phone number should be numeric.")
#         return phone
# # from django import forms
# # from django.contrib.auth.models import User
# # from django.contrib.gis.forms import PointField
# # from django.contrib.gis.geos import fromstr
# # from .models import Accommodation, Location

# # class AccommodationForm(forms.ModelForm):
# #     center = PointField(widget=forms.TextInput(attrs={'placeholder': 'POINT(longitude latitude)'}))
# #     images = forms.FileField(
# #         widget=forms.ClearableFileInput(attrs={'multiple': True}),
# #         required=False,
# #         help_text="Upload multiple property images."
# #     )
# #     country = forms.CharField(max_length=100, required=True)

# #     COUNTRY_CHOICES = [
# #         ('US', 'United States'),
# #         ('CA', 'Canada'),
# #         ('MX', 'Mexico'),
# #         # Add more countries as needed
# #     ]

# #     AMENITIES_CHOICES = [
# #         ('parking', 'Parking'),
# #         ('wifi', 'WiFi'),
# #         ('pool', 'Swimming Pool'),
# #         ('gym', 'Gym'),
# #         ('kitchen', 'Kitchen'),
# #     ]

# #     country_code = forms.ChoiceField(choices=COUNTRY_CHOICES)
# #     amenities = forms.MultipleChoiceField(
# #         choices=AMENITIES_CHOICES,
# #         widget=forms.CheckboxSelectMultiple,
# #         required=False
# #     )

# #     class Meta:
# #         model = Accommodation
# #         fields = [
# #             'title', 'country_code', 'country', 'bedroom_count', 
# #             'review_score', 'usd_rate', 'center', 'published', 
# #             'amenities', 'images'
# #         ]

# #     def clean_center(self):
# #         center = self.cleaned_data.get('center')
# #         try:
# #             point = fromstr(center)
# #             return point
# #         except Exception:
# #             raise forms.ValidationError("Invalid point format. Use 'POINT(longitude latitude)'")

# #     def clean_amenities(self):
# #         amenities = self.cleaned_data.get('amenities', [])
# #         return amenities
# from django import forms
# # from .models import Accommodation

# # class AccommodationForm(forms.ModelForm):
    
# #     images = forms.FileField(
# #         widget=forms.ClearableFileInput(attrs={'multiple': True}),
# #         required=False,
# #         help_text="Upload property images (multiple files allowed)"
# #     )
# #     class Meta:
# #         model = Accommodation
# #         fields = [
# #             'title', 'country_code', 'bedroom_count', 
# #             'review_score', 'usd_rate', 'amenities', 
# #             'published'
# #         ]
# #         widgets = {
# #             'amenities': forms.Textarea(attrs={'rows': 3}),
# #         }

    

# #     def clean_images(self):
# #         images = self.files.getlist('images')
# #         if images:
# #             for img in images:
# #                 # Add image validation if needed
# #                 if img.size > 5 * 1024 * 1024:  # 5MB limit
# #                     raise forms.ValidationError("Image size should not exceed 5MB")
# #         return images
# from django import forms
# from django.contrib.auth.models import User
# from .models import Accommodation, Location  # Correct relative import

# class AccommodationForm(forms.ModelForm):
#     images = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}),
#         required=False,
#         help_text="Upload property images (multiple files allowed)"
#     )

#     class Meta:
#         model = Accommodation
#         fields = [
#             'title', 'country_code', 'bedroom_count', 
#             'review_score', 'usd_rate', 'amenities', 
#             'published'
#         ]
#         widgets = {
#             'amenities': forms.Textarea(attrs={'rows': 3}),
#         }

#     def clean_images(self):
#         images = self.files.getlist('images')
#         if images:
#             for img in images:
#                 # Add image validation if needed
#                 if img.size > 5 * 1024 * 1024:  # 5MB limit
#                     raise forms.ValidationError("Image size should not exceed 5MB")
#         return images
from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator # type: ignore
from django.contrib.gis.forms import PointField # type: ignore

from .models import Accommodation, LocalizeAccommodation, Location

class BasePropertyForm(forms.ModelForm):
    """
    Base form for property-related models with common validations
    """
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        help_text="Upload property images (max 5MB per image)"
    )

    def clean_images(self):
        """
        Validate uploaded images
        """
        images = self.files.getlist('images')
        if images:
            for img in images:
                # 5MB file size limit
                if img.size > 5 * 1024 * 1024:  
                    raise ValidationError(f"Image {img.name} exceeds 5MB size limit")
        return images

    def clean_review_score(self):
        """
        Validate review score is between 0 and 5
        """
        review_score = self.cleaned_data.get('review_score')
        if review_score is not None and (review_score < 0 or review_score > 5):
            raise ValidationError("Review score must be between 0 and 5")
        return review_score

    def clean_bedroom_count(self):
        """
        Validate bedroom count is between 1 and 20
        """
        bedroom_count = self.cleaned_data.get('bedroom_count')
        if bedroom_count is not None and (bedroom_count < 1 or bedroom_count > 20):
            raise ValidationError("Bedroom count must be between 1 and 20")
        return bedroom_count

class PropertyForm(BasePropertyForm):
    """
    Form for Property model with enhanced validations
    """
    class Meta:
        model = Accommodation
        fields = [
            'feed', 'title', 'country_code', 'bedroom_count', 
            'review_score', 'usd_rate', 'center', 'images', 
            'location', 'amenities', 'published'
        ]

# class AccommodationForm(BasePropertyForm):
#     """
#     Form for Accommodation model with enhanced validations
#     """
#     class Meta:
#         model = Accommodation
#         fields = [
#             'title', 'country_code', 'bedroom_count', 
#             'review_score', 'usd_rate', 'amenities', 
#             'published'
#         ]
#         widgets = {
#             'amenities': forms.Textarea(attrs={'rows': 3}),
#         }
class AccommodationForm(forms.ModelForm):
    # Add an additional constructor to accept the request object
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Accept the request object
        super().__init__(*args, **kwargs)

    class Meta:
        model = Accommodation
        fields = ['id', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'center', 'images', 'location', 'amenities']
        exclude = ['id']
    def save(self, commit=True):
        accommodation = super().save(commit=False)
        if commit and self.request:
            accommodation.user = self.request.user  # Set the user to the currently logged-in user
            accommodation.save()
        return accommodation
class PropertyOwnerSignUpForm(forms.ModelForm):
    """
    Registration form for property owners with comprehensive validation
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(), 
        label="Password", 
        min_length=8,
        help_text="Password must be at least 8 characters long"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), 
        label="Confirm Password"
    )
    phone = forms.CharField(
        max_length=15,
        label="Phone Number",
        help_text="Numeric phone number"
    )
    location = forms.CharField(
        max_length=100,
        label="Location"
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        """
        Validate password confirmation
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2

    def clean_phone(self):
        """
        Validate phone number is numeric
        """
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits")
        return phone

    def clean_email(self):
        """
        Validate email uniqueness
        """
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")
        return email

    def save(self, commit=True):
        """
        Create user with hashed password
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    