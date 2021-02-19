# Generated by Django 3.1.5 on 2021-02-06 08:26

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('prdsolapp', '0004_auto_20210206_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Branch_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='City', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.branch'),
        ),
    ]
