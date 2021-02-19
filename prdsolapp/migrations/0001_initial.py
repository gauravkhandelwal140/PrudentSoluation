# Generated by Django 3.1.5 on 2021-02-06 08:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_name', models.CharField(max_length=130, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeySkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KeySkill_name', models.CharField(max_length=130, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vertical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vetical_name', models.CharField(max_length=130, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=150)),
                ('Middle_Name', models.CharField(blank=True, max_length=150, null=True)),
                ('Last_name', models.CharField(max_length=150, null=True)),
                ('Phone_no', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', message='Invalid mobile number')])),
                ('Alternative_Phone_no', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', message='Invalid mobile number')])),
                ('Email', models.EmailField(max_length=254, null=True, unique=True)),
                ('Cluster_head', models.CharField(max_length=50)),
                ('Team_leader', models.CharField(max_length=50)),
                ('CTC_in_Lacs', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('Bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.bank')),
                ('Branch_name', smart_selects.db_fields.ChainedForeignKey(chained_field='City', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.branch')),
                ('City', smart_selects.db_fields.ChainedForeignKey(chained_field='District', chained_model_field='district', on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.city')),
                ('Designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.designation')),
                ('District', smart_selects.db_fields.ChainedForeignKey(chained_field='State', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.district')),
                ('Grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.grade')),
                ('Key_Skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.keyskill')),
                ('State', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.state')),
                ('Vertical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.vertical')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='District',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='State', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.district'),
        ),
        migrations.AddField(
            model_name='city',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.state'),
        ),
        migrations.AddField(
            model_name='branch',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prdsolapp.city'),
        ),
        migrations.AlterUniqueTogether(
            name='district',
            unique_together={('state', 'district_name')},
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('cityname', 'District')},
        ),
    ]