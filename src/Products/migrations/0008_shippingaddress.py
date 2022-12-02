# Generated by Django 3.2.3 on 2021-07-09 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_rename_order_item_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=15, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('post_code', models.DecimalField(decimal_places=0, max_digits=6, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.order')),
            ],
        ),
    ]
