# Generated by Django 2.2.1 on 2019-05-25 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluadores', '0001_initial'),
        ('Evaluaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluadoresEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluaciones.Evaluacion')),
                ('evaluador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluadores.Evaluador')),
            ],
            options={
                'unique_together': {('evaluacion', 'evaluador')},
            },
        ),
    ]