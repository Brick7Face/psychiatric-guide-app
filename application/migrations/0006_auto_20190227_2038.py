# Generated by Django 2.1.7 on 2019-02-28 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20190227_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Organization'),
        ),
        migrations.AlterField(
            model_name='prescriber',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Organization'),
        ),
    ]
