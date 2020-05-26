# Generated by Django 2.2.7 on 2020-05-26 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=255)),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('submissionDeadline', models.DateField()),
                ('reviewDeadline', models.DateField()),
                ('conferenceDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(default='listener', max_length=32)),
                ('cId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Conference')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('accepted', models.BooleanField(null=True)),
                ('paperId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Abstract')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramCommitteeMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(default='listener', max_length=32)),
                ('cId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Conference')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ConferenceManager.Login')),
                ('name', models.CharField(max_length=32)),
                ('website', models.CharField(max_length=32)),
                ('affiliation', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SteeringCommittee',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ConferenceManager.Login')),
                ('name', models.CharField(max_length=32)),
                ('website', models.CharField(max_length=32)),
                ('affiliation', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='borderline', max_length=32)),
                ('justification', models.CharField(default='-', max_length=5000)),
                ('recommendations', models.CharField(default='-', max_length=5000)),
                ('paperId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Paper')),
                ('pcId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.ProgramCommitteeMember')),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pcId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.ProgramCommitteeMember')),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceAuthorSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conferenceAuthorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.ConferenceAuthor')),
                ('conferenceSessionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.ConferenceSession')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('chosenToReview', models.BooleanField(default=False)),
                ('abstractId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Abstract')),
                ('pcId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.ProgramCommitteeMember')),
            ],
        ),
        migrations.AddField(
            model_name='abstract',
            name='authorId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.ConferenceAuthor'),
        ),
        migrations.AddField(
            model_name='programcommitteemember',
            name='pEmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Participant'),
        ),
        migrations.AddField(
            model_name='conferenceauthor',
            name='pEmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceManager.Participant'),
        ),
    ]
