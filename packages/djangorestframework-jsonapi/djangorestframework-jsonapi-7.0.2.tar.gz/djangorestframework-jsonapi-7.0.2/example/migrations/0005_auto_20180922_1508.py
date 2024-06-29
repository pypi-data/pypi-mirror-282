# Generated by Django 2.1.1 on 2018-09-22 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("example", "0004_auto_20171011_0631"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.AlterModelOptions(
            name="artproject",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="researchproject",
            options={"base_manager_name": "objects"},
        ),
        migrations.AddField(
            model_name="project",
            name="project_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="example.ProjectType",
            ),
        ),
    ]
