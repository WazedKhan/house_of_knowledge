# Generated by Django 4.2.4 on 2023-09-17 17:20

import autoslug.fields
from django.db import migrations
import stock.utils


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=1,
                editable=False,
                populate_from=stock.utils.get_stock_slug,
                unique=True,
            ),
            preserve_default=False,
        ),
    ]