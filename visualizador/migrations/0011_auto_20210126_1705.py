# Generated by Django 3.1.4 on 2021-01-26 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualizador', '0010_auto_20210126_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancion',
            name='musico',
        ),
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visualizador.cancion')),
                ('musico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visualizador.musico')),
            ],
        ),
    ]
