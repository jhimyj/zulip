# Generated by Django 5.0.10 on 2025-01-13 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0648_remove_stream_stream_post_policy"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="can_add_subscribers_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]
