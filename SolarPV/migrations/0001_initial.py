# Generated by Django 2.2 on 2019-04-16 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('clientname', models.CharField(max_length=50)),
                ('clientType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('modelNum', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=50)),
                ('celltechnology', models.CharField(max_length=200)),
                ('cellmanufacture', models.DateField(blank=True, null=True)),
                ('numberofcells', models.IntegerField()),
                ('numberofcellsinseries', models.IntegerField()),
                ('numberofseriesinstrings', models.IntegerField()),
                ('numberofdiodes', models.IntegerField()),
                ('productlength', models.CharField(max_length=50)),
                ('productwidth', models.CharField(max_length=50)),
                ('productweight', models.CharField(max_length=50)),
                ('superstratetype', models.CharField(max_length=50)),
                ('superstratemanufacturer', models.CharField(max_length=50)),
                ('substratetype', models.CharField(max_length=50)),
                ('substratemanufacturer', models.CharField(max_length=50)),
                ('frametype', models.CharField(max_length=50)),
                ('frameadhesive', models.CharField(max_length=50)),
                ('encapsulanttype', models.CharField(max_length=50)),
                ('encapsulantmanufacturer', models.CharField(max_length=50)),
                ('junctionboxtype', models.CharField(max_length=50)),
                ('junctionboxmanufacturer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('sequenceID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('sequencename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('standardID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('serviceName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('publisheddate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('officephone', models.CharField(max_length=15)),
                ('cellphone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('prefix', models.CharField(choices=[('Dr.', 'DR.'), ('Mr.', 'MR.'), ('Mrs.', 'MRS.')], max_length=8)),
                ('clientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serviceID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('serviceName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('isFIrequired', models.CharField(max_length=50)),
                ('FIfrequency', models.CharField(max_length=50)),
                ('standardID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.TestStandard')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsystemvoltage', models.CharField(max_length=50)),
                ('opencircuitvoltage', models.CharField(max_length=50)),
                ('shortcircuitcurrent', models.CharField(max_length=50)),
                ('voltageatmaxpower', models.CharField(max_length=50)),
                ('currentatmaxpower', models.CharField(max_length=50)),
                ('maxpoweroutput', models.CharField(max_length=50)),
                ('fillfactor', models.CharField(max_length=50)),
                ('modelNum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.Product')),
                ('sequenceID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.TestSequence')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('address1', models.TextField(max_length=200)),
                ('address2', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postalcode', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=15)),
                ('faxnumber', models.CharField(max_length=15)),
                ('clientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificateID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('certnumber', models.CharField(max_length=50)),
                ('reportnumber', models.CharField(max_length=50)),
                ('issuedate', models.DateField(blank=True, null=True)),
                ('locationID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.Location')),
                ('modelNum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.Product')),
                ('standardID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.TestStandard')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolarPV.User')),
            ],
        ),
    ]
