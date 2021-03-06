# Generated by Django 3.0.8 on 2020-08-02 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('stars', models.IntegerField()),
                ('subtitle', models.CharField(max_length=60)),
                ('health', models.IntegerField()),
                ('faction', models.CharField(choices=[('AU', 'Autobot'), ('DE', 'Decepticon'), ('ME', 'Mercenary')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterTrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StratagemCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('stars', models.IntegerField()),
                ('target', models.CharField(max_length=60)),
                ('card_text', models.CharField(max_length=360)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterSide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('BOT', 'Bot Mode'), ('BOD', 'Body Mode'), ('COM', 'Combiner Mode'), ('ALT', 'Alt Mode'), ('CMB', 'Combiner Body Mode')], max_length=3)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('cardtext', models.CharField(max_length=360)),
                ('art', models.ImageField(blank=True, null=True, upload_to='art')),
                ('image', models.ImageField(editable=False, null=True, upload_to='cards')),
                ('charactercard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardmaker.CharacterCard')),
                ('traits', models.ManyToManyField(to='cardmaker.CharacterTrait')),
            ],
        ),
    ]
