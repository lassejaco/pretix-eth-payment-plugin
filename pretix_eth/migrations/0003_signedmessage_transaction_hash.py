# Generated by Django 3.2.12 on 2022-07-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretix_eth', '0002_auto_20220529_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='signedmessage',
            name='transaction_hash',
            field=models.CharField(max_length=66, null=True),
        ),
        migrations.AddField(
            model_name='signedmessage',
            name='safe_app_transaction_url',
            field=models.TextField(null=True),
        ),
    ]
