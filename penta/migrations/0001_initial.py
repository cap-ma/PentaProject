# Generated by Django 4.2 on 2023-04-29 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
                ('goals_scored', models.IntegerField()),
                ('goals_lost', models.IntegerField()),
                ('leag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penta.league')),
            ],
        ),
        migrations.CreateModel(
            name='Plays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('leag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penta.league')),
                ('name1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='name1', to='penta.teams')),
                ('name2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='name2', to='penta.teams')),
            ],
        ),
    ]