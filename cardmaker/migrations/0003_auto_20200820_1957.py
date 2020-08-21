# Generated by Django 3.0.8 on 2020-08-21 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardmaker', '0002_auto_20200801_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_text', models.CharField(max_length=360)),
                ('art', models.ImageField(blank=True, null=True, upload_to='art')),
                ('image', models.ImageField(editable=False, null=True, upload_to='')),
                ('name', models.CharField(blank=True, editable=False, max_length=60, null=True)),
                ('stars', models.IntegerField(blank=True, editable=False, null=True)),
                ('mode', models.CharField(choices=[('BOT', 'Bot Mode'), ('BOD', 'Body Mode'), ('COM', 'Combiner Mode'), ('ALT', 'Alt Mode'), ('CMB', 'Combiner Body Mode')], max_length=3)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='stratagemcard',
            name='image',
            field=models.ImageField(editable=False, null=True, upload_to=''),
        ),
        migrations.RenameModel(
            old_name='CharacterCard',
            new_name='Character',
        ),
        migrations.DeleteModel(
            name='CharacterSide',
        ),
        migrations.AddField(
            model_name='charactermode',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardmaker.Character'),
        ),
        migrations.AddField(
            model_name='charactermode',
            name='traits',
            field=models.ManyToManyField(to='cardmaker.CharacterTrait'),
        ),
    ]