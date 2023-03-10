# Generated by Django 4.1.5 on 2023-01-20 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VI_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='autumn_level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='VI_app.autumnlevel'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='spring_level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='VI_app.springlevel'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='summer_level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='VI_app.summerlevel'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='winter_level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='VI_app.winterlevel'),
        ),
    ]
