# Generated by Django 4.1.5 on 2023-01-30 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.brand')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.brand')),
                ('firm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.firm')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]