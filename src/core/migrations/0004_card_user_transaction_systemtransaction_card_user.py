# Generated by Django 4.2.4 on 2023-08-27 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_default_courses"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=16)),
                (
                    "currcency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.currency"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "auth_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=16)),
                ("time", models.DateTimeField()),
                (
                    "receiver_card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver_card_id",
                        to="core.card",
                    ),
                ),
                (
                    "sender_card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender_card_id",
                        to="core.card",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SystemTransaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=16)),
                ("note", models.CharField(max_length=100)),
                ("time", models.DateTimeField()),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.card"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="card",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.user"
            ),
        ),
    ]
