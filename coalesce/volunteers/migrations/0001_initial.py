# Generated by Django 3.0.8 on 2020-11-26 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField()),
                ('skills', models.TextField(help_text='List of skills the volunteer has')),
                ('organization', models.TextField(help_text="The volunteer's employer or organization")),
                ('organizer_comments', models.TextField()),
            ],
        ),
    ]