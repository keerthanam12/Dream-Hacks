# Generated by Django 4.0.8 on 2024-02-03 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managementsystem', '0010_quiz_quizquestion_quizanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('test_link', models.URLField()),
                ('questions', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managementsystem.quiz')),
            ],
        ),
        migrations.DeleteModel(
            name='Assignments',
        ),
    ]