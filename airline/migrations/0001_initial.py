# Generated by Django 5.0.4 on 2024-04-11 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Flight",
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
                ("origin_city", models.CharField(max_length=64)),
                ("origin_code", models.CharField(max_length=3)),
                ("origin_country", models.CharField(max_length=64)),
                ("destination_city", models.CharField(max_length=64)),
                ("destination_code", models.CharField(max_length=3)),
                ("destination_country", models.CharField(max_length=64)),
                ("depart_time", models.TimeField()),
                ("duration", models.DurationField()),
                ("plane", models.CharField(max_length=24)),
                ("airline", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Passenger",
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
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        default="O",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                    "seat_class",
                    models.CharField(
                        choices=[
                            ("economy", "Economy"),
                            ("business", "Business"),
                            ("first", "First"),
                        ],
                        max_length=20,
                    ),
                ),
                ("booking_date", models.DateTimeField(auto_now_add=True)),
                ("flight_ddate", models.DateField(blank=True, null=True)),
                ("flight_adate", models.DateField(blank=True, null=True)),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="airline.flight",
                    ),
                ),
                (
                    "passengers",
                    models.ManyToManyField(
                        related_name="flight_tickets", to="airline.passenger"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
