# Generated by Django 4.0 on 2022-05-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0004_tenders_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderAppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=255)),
                ('bid_amount', models.CharField(max_length=255)),
                ('tender_id', models.IntegerField()),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tender_appliers',
            },
        ),
    ]