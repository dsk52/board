# Generated by Django 2.1.2 on 2018-12-31 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_boardcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardcomment',
            old_name='board_id',
            new_name='board',
        ),
    ]
