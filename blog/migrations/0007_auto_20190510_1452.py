# Generated by Django 2.2.1 on 2019-05-10 18:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190510_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('código', models.CharField(max_length=6)),
                ('sección', models.CharField(max_length=1)),
                ('año', models.PositiveSmallIntegerField()),
                ('semestre', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluación',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_min', models.IntegerField(default=5)),
                ('tiempo_max', models.IntegerField(default=8)),
                ('fecha_inicio', models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 10, 18, 52, 38, 933071, tzinfo=utc))),
                ('fecha_fin', models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 10, 18, 52, 38, 933118, tzinfo=utc))),
                ('estado', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Curso')),
                ('rubrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Rubrica')),
            ],
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='rubrica',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Curso'),
        ),
        migrations.AlterField(
            model_name='fichaevaluacion',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Evaluación'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Curso'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Evaluacion',
        ),
    ]
