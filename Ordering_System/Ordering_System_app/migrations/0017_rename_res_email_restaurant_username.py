# Generated by Django 4.2.6 on 2023-11-07 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering_System_app', '0016_websiteinfo_web_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='Res_Email',
            new_name='username',
        ),
    ]
