# Generated by Django 5.1.2 on 2024-11-19 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evento_proy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concierto',
            old_name='artista',
            new_name='_artista',
        ),
        migrations.RenameField(
            model_name='concierto',
            old_name='duracion',
            new_name='_duracion',
        ),
        migrations.RenameField(
            model_name='conferencia',
            old_name='orador',
            new_name='_orador',
        ),
        migrations.RenameField(
            model_name='conferencia',
            old_name='tema',
            new_name='_tema',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='fecha',
            new_name='_fecha',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='lugar',
            new_name='_lugar',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='nombre',
            new_name='_nombre',
        ),
    ]
