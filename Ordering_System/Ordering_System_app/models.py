from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models


# from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    Cate_id = models.AutoField(primary_key=True)
    Cate_Name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Cate_Name


class Area(models.Model):
    Ar_id = models.AutoField(primary_key=True)
    Ar_Name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Ar_Name


class Restaurant(models.Model):
    Res_id = models.AutoField(primary_key=True)
    cate_id = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    Res_Name = models.CharField(max_length=100, unique=True)
    Res_img = models.FileField(upload_to='Res_img/', blank=True, null=True, default='')
    Res_Email = models.CharField(max_length=100)
    # Res_Password = models.CharField(max_length=50)
    Res_Phone = models.CharField(max_length=50)
    Ar_id = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    Res_Address = models.CharField(max_length=250)
    Res_MenuFile = models.FileField(upload_to='menu/', blank=True, null=True, default='')
    Res_OpenAT = models.DateTimeField()
    Res_CloseAT = models.DateTimeField()

    # Replace 'email' with the appropriate field that should serve as the username
    USERNAME_FIELD = 'Res_Email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.Res_Name


class CustomOwnerCreationForm(UserCreationForm):
    # Custom fields for the Restaurant model
    # cate_id = forms.ModelChoiceField(
    #     queryset=category.objects.all(),
    #     label="Food Category",
    #     required=False,
    #     empty_label="Select a Category",
    # )

    Res_Name = forms.CharField(max_length=100, label="Restaurant Name")

    Res_Email = forms.EmailField(label="Restaurant Email")
    Res_Phone = forms.CharField(max_length=50, label="Phone")
    # Ar_id = forms.ModelChoiceField(
    #     queryset=Area.objects.all(), label="Area",
    #     required=False,
    #     empty_label="Select an Area",
    # )
    Res_Address = forms.CharField(max_length=250, label="Address")
    # Res_Password = forms.CharField(max_length=50, label="Password")

    class Meta:
        model = Restaurant
        fields = [
            'Res_Name',
            'Res_Email',
            'Res_Phone',
            'Res_Address',
        ]
        # Replace 'email' with the appropriate field that should serve as the username
        USERNAME_FIELD = 'Res_Email'
        REQUIRED_FIELDS = []

    def save(self, commit=True):
        user = super(CustomOwnerCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class dish(models.Model):
    Dish_id = models.AutoField(primary_key=True)
    Dish_Name = models.CharField(max_length=50, unique=True)
    Dish_img = models.ImageField(upload_to='dish_img/', blank=True, null=True, default='')
    Dish_Des = models.CharField(max_length=255)
    cate_id = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    Res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    Dish_Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Dish_Name


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CartItem(models.Model):
    dish_name = models.ForeignKey(dish, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)


class Contact_msg(models.Model):
    Con_id = models.AutoField(primary_key=True)
    Con_Name = models.CharField(max_length=50, blank=False, null=False)
    Con_Email = models.CharField(max_length=50, blank=False, null=False)
    Con_msg = models.CharField(max_length=255)

    def __str__(self):
        return self.Con_Name


class WebsiteInfo(models.Model):
    Web_id = models.AutoField(primary_key=True)
    Web_name = models.CharField(max_length=50, null=True)
    Web_address = models.CharField(max_length=50)
    Web_email = models.CharField(max_length=50)
    Web_phone = models.CharField(max_length=50)
    Web_facebook_link = models.CharField(max_length=50)
    Web_instagram_link = models.CharField(max_length=50)
    Web_twitter_link = models.CharField(max_length=50)
    Web_whatsapp_link = models.CharField(max_length=50)
