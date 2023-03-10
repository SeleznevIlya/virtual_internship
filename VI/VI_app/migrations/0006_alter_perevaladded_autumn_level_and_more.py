# Generated by Django 4.1.5 on 2023-01-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VI_app', '0005_rename_coord_id_perevaladded_coord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='autumn_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.autumnlevel'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='spring_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.springlevel'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='summer_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.summerlevel'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='winter_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.winterlevel'),
        ),
    ]
