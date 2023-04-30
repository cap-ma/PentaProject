# Generated by Django 4.2 on 2023-04-30 04:51

from django.db import migrations, models
import penta.models


class Migration(migrations.Migration):

    dependencies = [
        ('penta', '0003_news_text_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='logo',
            field=models.ImageField(default='', upload_to=penta.models.upload_logo_to),
            preserve_default=False,
        ),
    ]