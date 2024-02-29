# Generated by Django 4.2.6 on 2023-10-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Res_id', models.IntegerField()),
                ('Res_Name', models.CharField(max_length=100)),
                ('Res_Email', models.CharField(max_length=100)),
                ('Res_Password', models.CharField(max_length=50)),
                ('Res_Phone', models.IntegerField()),
                ('Res_Address', models.CharField(max_length=250)),
                ('Res_MenuFile', models.FileField(blank=True, default='', null=True, upload_to='menu/')),
                ('Res_OpenAT', models.DateTimeField()),
                ('Res_CloseAT', models.DateTimeField()),
            ],
        ),
    ]
