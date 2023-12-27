# Generated by Django 5.0 on 2023-12-24 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_user_bids_remove_comment_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('active', models.BooleanField()),
                ('categorie', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.listing')),
            ],
        ),
    ]
