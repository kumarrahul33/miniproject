# Generated by Django 4.0.4 on 2022-04-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookissue', '0002_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('avl', models.BooleanField(default=True)),
                ('issued_to', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
