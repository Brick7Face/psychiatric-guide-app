# Generated by Django 2.1.5 on 2019-02-11 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_step_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='treatment',
            field=models.ForeignKey(default='incomplete', on_delete=django.db.models.deletion.DO_NOTHING, to='application.Treatment'),
        ),
    ]