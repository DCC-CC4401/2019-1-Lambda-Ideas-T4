# Generated by Django 2.2.1 on 2019-05-16 23:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rubricas', '0002_auto_20190516_1854'),
        ('Evaluadores', '0001_initial'),
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_min', models.IntegerField(default=5)),
                ('tiempo_max', models.IntegerField(default=8)),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_fin', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.Curso')),
                ('rubrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rubricas.Rubrica')),
            ],
        ),
        migrations.CreateModel(
            name='FichaEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_grupo', models.CharField(max_length=15)),
                ('estado_evaluacion', models.CharField(max_length=15)),
                ('tiempo', models.IntegerField(default=0)),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluaciones.Evaluacion')),
                ('evaluador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluadores.Evaluador')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.Grupo')),
                ('presentador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.Alumno')),
                ('rubrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rubricas.AspectoRubrica')),
            ],
        ),
    ]