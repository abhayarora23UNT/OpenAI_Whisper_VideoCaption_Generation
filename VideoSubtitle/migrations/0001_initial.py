# Generated by Django 4.1.7 on 2023-02-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSubtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('video', models.FileField(null=True, upload_to='videos/%y', verbose_name='')),
            ],
        ),
    ]
