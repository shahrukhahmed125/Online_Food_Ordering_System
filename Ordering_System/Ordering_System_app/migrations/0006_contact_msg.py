# Generated by Django 4.2.6 on 2023-10-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering_System_app', '0005_dish_restaurant_dish_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_msg',
            fields=[
                ('Con_id', models.AutoField(primary_key=True, serialize=False)),
                ('Con_Name', models.CharField(max_length=50)),
                ('Con_Email', models.CharField(max_length=50)),
                ('Con_msg', models.CharField(max_length=255)),
            ],
        ),
    ]
