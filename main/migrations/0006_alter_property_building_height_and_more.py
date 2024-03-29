# Generated by Django 4.1.7 on 2023-04-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_property_building_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='building_height',
            field=models.CharField(choices=[('1', 'Lowrise (1 to 4 storeys)'), ('0.5', 'Midrise (5 to 15 storeys)'), ('0', 'Highrise (at least 16 storeys or 48 meters high)')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='building_insurance',
            field=models.CharField(choices=[('1', 'Insured'), ('0.5', 'Incomplete insurance (e.g. has fire insurance but no earthquake insurance)'), ('0', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='disaster_history',
            field=models.CharField(choices=[('1', 'It withstood the disaster and did not need to undergo repairs'), ('0.5', 'The building withstood some minor damage but it has been properly repaires since then'), ('0', 'There was grave damage and it has not been properly repaired')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='essential_institutions',
            field=models.CharField(choices=[('1', 'Nearby'), ('0.5', 'Not too far'), ('0', 'Far away')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='evacuation_zone',
            field=models.CharField(choices=[('1', 'Nearby'), ('0.5', 'Not too far'), ('0', 'Far away')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='fire_exits',
            field=models.CharField(choices=[('1', 'Fully-functional'), ('0.5', 'Signs of aging and needs upkeep but no worrisome'), ('0', 'Completely impassable, worrisome decline')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='gas_valve',
            field=models.CharField(choices=[('1', 'Fully-functional'), ('0', 'Faulty')], max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='soil',
            field=models.CharField(choices=[('1', 'Firm soil'), ('0.5', 'Unsure'), ('0', 'Loose soil')], max_length=255),
        ),
    ]
