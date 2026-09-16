from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone must contain 10 to 15 digits.', regex='^\\d{10,15}$')])),
                ('department', models.CharField(choices=[('Engineering','Engineering'),('HR','HR'),('QA','QA'),('DevOps','DevOps'),('Finance','Finance'),('Marketing','Marketing'),('Sales','Sales'),('Support','Support'),('Management','Management')], max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField()),
                ('salary', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('status', models.CharField(choices=[('Active','Active'),('On Leave','On Leave'),('Resigned','Resigned')], default='Active', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
