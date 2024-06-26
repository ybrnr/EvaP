# Generated by Django 5.0.6 on 2024-06-17 23:00

import django_fsm
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0143_alter_evaluation_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="state",
            field=django_fsm.FSMIntegerField(
                choices=[
                    (10, "new"),
                    (20, "prepared"),
                    (30, "editor approved"),
                    (40, "approved"),
                    (50, "in evaluation"),
                    (60, "evaluated"),
                    (70, "reviewed"),
                    (80, "published"),
                ],
                default=10,
                protected=True,
                verbose_name="state",
            ),
        ),
    ]
