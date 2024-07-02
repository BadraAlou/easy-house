# Generated by Django 5.0.3 on 2024-07-02 09:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("status", models.IntegerField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Position",
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
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("status", models.IntegerField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
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
                ("code", models.CharField(blank=True, max_length=100)),
                ("firstname", models.TextField()),
                ("middlename", models.TextField(blank=True, null=True)),
                ("lastname", models.TextField()),
                ("gender", models.TextField(blank=True, null=True)),
                ("dob", models.DateField(blank=True, null=True)),
                ("contact", models.TextField()),
                ("address", models.TextField()),
                ("email", models.TextField()),
                ("date_hired", models.DateField()),
                ("salary", models.FloatField(default=0)),
                ("status", models.IntegerField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "department_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee_information.department",
                    ),
                ),
                (
                    "position_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee_information.position",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("amount", models.FloatField()),
                (
                    "payment_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee_information.employees",
                    ),
                ),
            ],
        ),
    ]
