# Generated by Django 4.1.5 on 2023-01-19 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AutumnLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalActivitiesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.activitiestype')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('other_title', models.CharField(max_length=255)),
                ('connect', models.BooleanField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', '??????????'), ('pending', '?? ????????????'), ('accepted', '????????????????'), ('rejected', '??????????????????')], default='new', max_length=20)),
                ('activities_types', models.ManyToManyField(through='VI_app.PerevalActivitiesType', to='VI_app.activitiestype')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areas', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SpringLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SummerLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WinterLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('pereval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.perevaladded')),
            ],
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='areas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.perevalareas'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='autumn_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.autumnlevel'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='coord_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='VI_app.coords'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='spring_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.springlevel'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='summer_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.summerlevel'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='winter_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.winterlevel'),
        ),
        migrations.AddField(
            model_name='perevalactivitiestype',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VI_app.perevaladded'),
        ),
    ]
