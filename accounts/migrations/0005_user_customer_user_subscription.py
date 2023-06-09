# Generated by Django 4.1.7 on 2023-03-20 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0011_2_7'),
        ('accounts', '0004_alter_user_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.subscription'),
        ),
    ]
