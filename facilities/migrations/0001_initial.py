# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models.base
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
import common.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'This is the official name of the facility', unique=True, max_length=100)),
                ('code', common.fields.SequenceField(help_text=b'A sequential number allocated to each facility', unique=True, editable=False, blank=True)),
                ('abbreviation', models.CharField(help_text=b'A short name for the facility.', max_length=30, null=True, blank=True)),
                ('description', models.TextField(help_text=b'A brief summary of the Facility')),
                ('location_desc', models.TextField(help_text=b'This field allows a more detailed description of how tolocate the facility e.g Joy medical clinic is in Jubilee Plaza7th Floor')),
                ('number_of_beds', models.PositiveIntegerField(default=0, help_text=b'The number of beds that a facilty has. e.g 0')),
                ('number_of_cots', models.PositiveIntegerField(default=0, help_text=b'The number of cots that a facility has e.g 0')),
                ('open_whole_day', models.BooleanField(default=False, help_text=b'Is the facility open 24 hours a day?')),
                ('open_whole_week', models.BooleanField(default=False, help_text=b'Is the facility open the entire week?')),
                ('is_classified', models.BooleanField(default=False, help_text=b"Should the facility geo-codes be visible to the public?Certain facilities are kept 'off-the-map'")),
                ('is_published', models.BooleanField(default=False, help_text=b'Should be True if the facility is to be seen on the public MFL site')),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'facilities',
            },
            bases=(models.Model, common.models.base.SequenceMixin),
        ),
        migrations.CreateModel(
            name='FacilityContact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('contact', models.ForeignKey(to='common.Contact', on_delete=django.db.models.deletion.PROTECT)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(to='facilities.Facility', on_delete=django.db.models.deletion.PROTECT)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacilityCoordinates',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('latitude', models.CharField(help_text=b'How far north or south a facility is from the equator', max_length=255)),
                ('longitude', models.CharField(help_text=b'How far east or west one a facility is from the Greenwich Meridian', max_length=255)),
                ('collection_date', models.DateTimeField()),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('facility', models.OneToOneField(to='facilities.Facility')),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name': 'facility coordinates',
                'verbose_name_plural': 'facility coordinates',
            },
        ),
        migrations.CreateModel(
            name='FacilityRegulationStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('reason', models.TextField(help_text=b'e.g Why has a facility been suspended', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(related_name='regulatory_details', on_delete=django.db.models.deletion.PROTECT, to='facilities.Facility')),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'facility regulation statuses',
            },
        ),
        migrations.CreateModel(
            name='FacilityStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'A short name respresenting the operanation status e.g OPERATIONAL', unique=True, max_length=100)),
                ('description', models.TextField(help_text=b'A short explanation of what the status entails.')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'facility statuses',
            },
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'A short unique name for the facility type e.g DISPENSARY', unique=True, max_length=100)),
                ('sub_division', models.CharField(help_text=b'This is a further division of the facility type e.g Hospitals can be further divided into District hispitals and Provincial Hospitals.', max_length=100, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacilityUnit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text=b'A short summary of the facility unit.')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(to='facilities.Facility', on_delete=django.db.models.deletion.PROTECT)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeoCodeMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'The name of the method.', max_length=100)),
                ('description', models.TextField(help_text=b'A short description of the method', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeoCodeSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'The name of the collecting organization', max_length=100)),
                ('description', models.TextField(help_text=b'A short summary of the collecting organization', null=True, blank=True)),
                ('abbreviation', models.CharField(help_text=b'An acronym of the collecting or e.g SAM', max_length=10)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'A short name for the job title', max_length=100)),
                ('description', models.TextField(help_text=b'A short summary of the job title')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfficerIncharge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'the name of the officer in-charge e.g Roselyne Wiyanga ', max_length=150)),
                ('registration_number', models.CharField(help_text=b'This is the licence number of the officer. e.g for a nurse use the NCK registration number.', max_length=100)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'officers in charge',
            },
        ),
        migrations.CreateModel(
            name='OfficerInchargeContact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Contact', help_text=b'The contact of the officer incharge may it be email,  mobile number etc')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facilities.OfficerIncharge', help_text=b'The is the officer in charge')),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'The name of owner e.g Ministry of Health.', unique=True, max_length=100)),
                ('description', models.TextField(help_text=b'A brief summary of the owner.', null=True, blank=True)),
                ('code', common.fields.SequenceField(help_text=b'A unique number to identify the owner.Could be up to 7 characteres long.', unique=True, editable=False, blank=True)),
                ('abbreviation', models.CharField(help_text=b'Short form of the name of the owner e.g Ministry of health could be shortened as MOH', max_length=10, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
            bases=(models.Model, common.models.base.SequenceMixin),
        ),
        migrations.CreateModel(
            name='OwnerType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'Short unique name for a particular type of owners. e.g INDIVIDUAL', max_length=100)),
                ('description', models.TextField(help_text=b'A brief summary of the particular type of owner.', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegulatingBody',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'The name of the regulating body', unique=True, max_length=100)),
                ('abbreviation', models.CharField(help_text=b'A shortform of the name of the regulating body e.g NursingCouncil of Kenya could be abbreviated as NCK.', max_length=10, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'regulating bodies',
            },
        ),
        migrations.CreateModel(
            name='RegulationStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'A short unique name representing a state/stage of regulation e.g. PENDING_OPENING ', unique=True, max_length=100)),
                ('description', models.TextField(help_text=b"A short description of the regulation state or state e.gPENDING_OPENING could be descriped as 'waiting for the license tobegin operating' ")),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'regulation_statuses',
            },
        ),
        migrations.AddField(
            model_name='owner',
            name='owner_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facilities.OwnerType', help_text=b'The classification of the owner e.g INDIVIDUAL'),
        ),
        migrations.AddField(
            model_name='owner',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='officerincharge',
            name='contacts',
            field=models.ManyToManyField(help_text=b'Personal contacts of the officer in charge', to='common.Contact', through='facilities.OfficerInchargeContact'),
        ),
        migrations.AddField(
            model_name='officerincharge',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='officerincharge',
            name='job_title',
            field=models.ForeignKey(to='facilities.JobTitle', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='officerincharge',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facilityregulationstatus',
            name='regulating_body',
            field=models.ForeignKey(to='facilities.RegulatingBody', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='facilityregulationstatus',
            name='regulation_status',
            field=models.ForeignKey(to='facilities.RegulationStatus', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='facilityregulationstatus',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facilitycoordinates',
            name='method',
            field=models.ForeignKey(help_text=b'Method used to obtain the geo codes. e.g taken with GPS device', to='facilities.GeoCodeMethod'),
        ),
        migrations.AddField(
            model_name='facilitycoordinates',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facilities.GeoCodeSource', help_text=b'where the geo code came from'),
        ),
        migrations.AddField(
            model_name='facilitycoordinates',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facility',
            name='contacts',
            field=models.ManyToManyField(help_text=b'Facility contacts - email, phone, fax, postal etc', to='common.Contact', through='facilities.FacilityContact'),
        ),
        migrations.AddField(
            model_name='facility',
            name='created_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facility',
            name='facility_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='facilities.FacilityType', help_text=b'This depends on who owns the facilty. For MOH facilities,type is the gazetted classification of the facilty.For Non-MOH check under the respective owners.'),
        ),
        migrations.AddField(
            model_name='facility',
            name='officer_in_charge',
            field=models.ForeignKey(help_text=b'The officer in charge of the facility', to='facilities.OfficerIncharge'),
        ),
        migrations.AddField(
            model_name='facility',
            name='operation_status',
            field=models.OneToOneField(to='facilities.FacilityStatus', help_text=b'Indicates whether the facilityhas been approved to operate, is operating, is temporarilynon-operational, or is closed down'),
        ),
        migrations.AddField(
            model_name='facility',
            name='owner',
            field=models.ForeignKey(help_text=b'A link to the organization that owns the facility', to='facilities.Owner'),
        ),
        migrations.AddField(
            model_name='facility',
            name='parent',
            field=models.ForeignKey(blank=True, to='facilities.Facility', help_text=b'Indicates the umbrella facility of a facility', null=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='physical_address',
            field=models.ForeignKey(help_text=b'Postal and courier addressing for the facility', to='common.PhysicalAddress'),
        ),
        migrations.AddField(
            model_name='facility',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facility',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Ward', help_text=b'County ward in which the facility is located'),
        ),
        migrations.AlterUniqueTogether(
            name='facilitytype',
            unique_together=set([('name', 'sub_division')]),
        ),
    ]
