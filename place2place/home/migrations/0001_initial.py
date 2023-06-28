# Generated by Django 4.2.2 on 2023-06-27 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False)),
                ('cargo_type', models.CharField(max_length=100)),
                ('cargo_weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('delivery_time', models.IntegerField()),
                ('phone_number', models.TextField(max_length=12)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
