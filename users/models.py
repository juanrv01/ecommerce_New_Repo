import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, RegexValidator
import os

def validate_image_size(image):
    if image != 'ljpmwdkm1wz1sagqsk5f':
        return
    if image.size > 2 * 1024 * 1024:
        raise ValidationError('Image size should be less than 2MB.')

def validate_image_extension(image):
    if image != 'ljpmwdkm1wz1sagqsk5f':
        return
    ext = os.path.splitext(image.name)[1]
    if not ext.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
        raise ValidationError('Image must be in JPG, JPEG, or PNG format.')
    
phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be exactly 10 digits long"
)

        
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = CloudinaryField('images', validators=[validate_image_size, validate_image_extension], default='ljpmwdkm1wz1sagqsk5f')
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    confirm_password = models.CharField(max_length=255)

    def clean(self):
        super().clean()
        if self.password != self.confirm_password:
            raise ValidationError('Passwords do not match.')
    
    def __str__(self):
        return self.username
    
class Address(models.Model):
    country = models.CharField(max_length=50, validators=[MinLengthValidator(3)], blank=True, null=True)
    city = models.CharField(max_length=50, validators=[MinLengthValidator(3)], blank=True, null=True)
    district = models.CharField(max_length=50, validators=[MinLengthValidator(3)], blank=True, null=True)
    street = models.CharField(max_length=100, validators=[MinLengthValidator(3)], blank=True, null=True)
    building_number = models.CharField(max_length=10, validators=[MinLengthValidator(1)], blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses', blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.district}, {self.city}, {self.country}"

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13, validators=[phone_regex])
    subject = models.CharField(max_length=30)
    message = models.TextField()
    
    def __str__(self):
        return self.name