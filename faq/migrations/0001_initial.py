from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question in English')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('question_hi', models.TextField(verbose_name='Question in Hindi', blank=True, null=True)),
                ('question_bn', models.TextField(verbose_name='Question in Bengali', blank=True, null=True)),
                ('language', models.CharField(max_length=2, choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali')], default='en', verbose_name='Language')),
            ],
        ),
    ]