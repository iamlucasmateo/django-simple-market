# Generated by Django 4.1.7 on 2023-04-02 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                default=1,
                max_length=255,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="items.category",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]