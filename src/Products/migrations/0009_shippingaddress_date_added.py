# Generated by Django 3.2.3 on 2021-07-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
