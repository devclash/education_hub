# Generated by Django 3.1.1 on 2020-09-02 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0003_remove_question_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
            ],
        ),
    ]
