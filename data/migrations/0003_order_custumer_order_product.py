# Generated by Django 4.2.1 on 2023-08-10 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.custumer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.product'),
        ),
    ]
