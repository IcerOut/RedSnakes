# Generated by Django 2.2.4 on 2020-05-02 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ConferenceManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChairMember',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.User')),
            ],
            bases=('ConferenceManager.user',),
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.User')),
            ],
            bases=('ConferenceManager.user',),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.User')),
            ],
            bases=('ConferenceManager.user',),
        ),
        migrations.RenameField(
            model_name='user',
            old_name='photoURL',
            new_name='userName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='street',
            new_name='webPage',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='coordsX',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='coordsY',
        ),
        migrations.RemoveField(
            model_name='user',
            name='locationX',
        ),
        migrations.RemoveField(
            model_name='user',
            name='locationY',
        ),
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('chairmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.ChairMember')),
            ],
            bases=('ConferenceManager.chairmember',),
        ),
        migrations.CreateModel(
            name='CoChair',
            fields=[
                ('chairmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.ChairMember')),
            ],
            bases=('ConferenceManager.chairmember',),
        ),
        migrations.CreateModel(
            name='PcMember',
            fields=[
                ('chairmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.ChairMember')),
            ],
            bases=('ConferenceManager.chairmember',),
        ),
        migrations.CreateModel(
            name='ScMember',
            fields=[
                ('chairmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ConferenceManager.ChairMember')),
            ],
            bases=('ConferenceManager.chairmember',),
        ),
    ]