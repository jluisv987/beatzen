# Generated by Django 3.1.4 on 2021-01-26 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualizador', '0013_invitado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='musico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visualizador.musico'),
        ),
        migrations.DeleteModel(
            name='Invitado',
        ),
    ]
