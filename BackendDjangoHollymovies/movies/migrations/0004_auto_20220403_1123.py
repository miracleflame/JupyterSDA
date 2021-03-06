# Generated by Django 3.2.12 on 2022-04-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220402_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
                ('born_at', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movies.director'),
        ),
    ]
