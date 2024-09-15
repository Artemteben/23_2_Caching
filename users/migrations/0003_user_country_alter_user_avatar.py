# Generated by Django 4.2.2 on 2024-09-02 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Country"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="users/avatars/",
                verbose_name="Фотография профиля",
            ),
        ),
    ]
