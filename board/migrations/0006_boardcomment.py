# Generated by Django 2.1.2 on 2018-11-11 09:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_board_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
            ],
            options={
                'db_table': 'board_comment',
            },
        ),
    ]