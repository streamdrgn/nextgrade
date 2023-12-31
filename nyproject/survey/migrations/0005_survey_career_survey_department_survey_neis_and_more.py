# Generated by Django 4.2.7 on 2023-11-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_remove_survey_career_remove_survey_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='career',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='department',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='neis',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='survey',
            name='subject',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='survey',
            name='name',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
