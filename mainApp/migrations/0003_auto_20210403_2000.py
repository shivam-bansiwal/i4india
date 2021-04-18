# Generated by Django 3.1.7 on 2021-04-03 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20210327_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirCooler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='aircoolerproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('power', models.CharField(max_length=80)),
                ('rating', models.CharField(max_length=80)),
                ('airFlowCapacity', models.CharField(max_length=80)),
                ('coolingPad', models.CharField(max_length=80)),
                ('tankCapacity', models.CharField(max_length=80)),
                ('standardRoomDimension', models.CharField(max_length=80)),
                ('waterConsumption', models.CharField(max_length=80)),
                ('windSpeed', models.CharField(max_length=80)),
                ('coolingHeating', models.CharField(max_length=80)),
                ('feature', models.CharField(max_length=150)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='AttaChakki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='attachakkiproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('HP', models.CharField(max_length=80)),
                ('LBH', models.CharField(max_length=80)),
                ('weight', models.CharField(max_length=80)),
                ('grindingCapacity', models.CharField(max_length=80)),
                ('hopperCapacity', models.CharField(max_length=80)),
                ('powerConsumption', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeTheater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('colour', models.CharField(max_length=80)),
                ('supportsUSB_AD_AUX_FM_Bluetooth', models.CharField(max_length=80)),
                ('LEDDisplay', models.CharField(max_length=80)),
                ('wooferSpeakerDrive', models.CharField(max_length=80)),
                ('impedance', models.CharField(max_length=80)),
                ('remoteSensitivity', models.CharField(max_length=80)),
                ('inputPowerRange', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='HotPlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='hotplateproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('power', models.CharField(max_length=80)),
                ('rating', models.CharField(max_length=80)),
                ('inputVoltage', models.CharField(max_length=80)),
                ('powerIndicator', models.CharField(max_length=80)),
                ('temperatureAdjuster', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Iron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=80)),
                ('colour', models.CharField(max_length=80)),
                ('bodyMaterial', models.CharField(max_length=80)),
                ('corded', models.CharField(max_length=80)),
                ('swivelCord', models.CharField(max_length=80)),
                ('indicatorLight', models.CharField(max_length=80)),
                ('tempratureControl', models.CharField(max_length=80)),
                ('solePlateType', models.CharField(max_length=80)),
                ('power', models.CharField(max_length=80)),
                ('voltage', models.CharField(max_length=80)),
                ('dimensions', models.CharField(max_length=80)),
                ('weight', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='JuicerMixer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('colour', models.CharField(max_length=80)),
                ('power', models.CharField(max_length=80)),
                ('rating', models.CharField(max_length=80)),
                ('stainlessSteelJar', models.CharField(max_length=80)),
                ('copperMotor', models.CharField(max_length=80)),
                ('feature', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='JuicerMixerGrinder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=80)),
                ('capacity', models.CharField(max_length=80)),
                ('colour', models.CharField(max_length=80)),
                ('noOfJars', models.CharField(max_length=80)),
                ('functions', models.CharField(max_length=80)),
                ('bodyShape', models.CharField(max_length=80)),
                ('bodyMaterial', models.CharField(max_length=80)),
                ('jarMaterial', models.CharField(max_length=80)),
                ('bladeMaterial', models.CharField(max_length=80)),
                ('noOfSpeedSettings', models.CharField(max_length=80)),
                ('chutneyJar', models.CharField(max_length=80)),
                ('mainJai', models.CharField(max_length=80)),
                ('middleJar', models.CharField(max_length=80)),
                ('features', models.CharField(max_length=80)),
                ('power', models.CharField(max_length=80)),
                ('voltage', models.CharField(max_length=80)),
                ('rating', models.CharField(max_length=80)),
                ('dimensions', models.CharField(max_length=80)),
                ('weigth', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='refrigeratorproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('capacity', models.CharField(max_length=80)),
                ('starRating', models.CharField(max_length=80)),
                ('coolingTechnology', models.CharField(max_length=80)),
                ('colour', models.CharField(max_length=80)),
                ('inverterCompressor', models.CharField(max_length=80)),
                ('defrostingType', models.CharField(max_length=80)),
                ('exteriors', models.CharField(max_length=80)),
                ('noOfShelves', models.CharField(max_length=80)),
                ('specialCompartments', models.CharField(max_length=80)),
                ('shelvesType', models.CharField(max_length=80)),
                ('vegetableBasket', models.CharField(max_length=80)),
                ('dimensions', models.CharField(max_length=80)),
                ('weightinKg', models.CharField(max_length=80)),
                ('unitWarranty', models.CharField(max_length=80)),
                ('compressorWarranty', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='TowerTheater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='ironproductimages/')),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('colour', models.CharField(max_length=80)),
                ('speakerDriveRangeSize', models.CharField(max_length=80)),
                ('tweeterType', models.CharField(max_length=80)),
                ('impedance', models.CharField(max_length=80)),
                ('frequencyResponseRange', models.CharField(max_length=80)),
                ('tweeter', models.CharField(max_length=80)),
                ('SNratio', models.CharField(max_length=80)),
                ('sepration', models.CharField(max_length=80)),
                ('sensitivity', models.CharField(max_length=80)),
                ('remoteSensitivity', models.CharField(max_length=80)),
                ('inputPowerRange', models.CharField(max_length=80)),
                ('feature', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('img6', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('img7', models.ImageField(blank=True, default=None, null=True, upload_to='tvproductimages/')),
                ('screenSize', models.CharField(max_length=80)),
                ('brand', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('screenType', models.CharField(max_length=80)),
                ('resolution', models.CharField(max_length=80)),
                ('refreshRate', models.CharField(max_length=80)),
                ('hdmi', models.CharField(max_length=80)),
                ('blueRayPlayers', models.CharField(max_length=80)),
                ('gamingConsole', models.CharField(max_length=80)),
                ('sound', models.CharField(max_length=80)),
                ('megaContrast', models.CharField(max_length=80)),
                ('purcolor', models.CharField(max_length=80)),
                ('pictureQuality', models.CharField(max_length=80)),
                ('design', models.CharField(max_length=80)),
                ('speaker', models.CharField(max_length=80)),
                ('usb', models.CharField(max_length=80)),
                ('compositeIn', models.CharField(max_length=80)),
                ('headphoneOut', models.CharField(max_length=80)),
                ('wallMount', models.CharField(max_length=80)),
                ('additionalFeatures', models.CharField(max_length=80)),
                ('powerSupply', models.CharField(max_length=80)),
                ('standby', models.CharField(max_length=80)),
                ('dimensions', models.CharField(max_length=80)),
                ('weightinKg', models.CharField(max_length=80)),
                ('warrantyPeriod', models.CharField(max_length=80)),
                ('warrantyType', models.CharField(max_length=80)),
                ('boxContent', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='juicermixergrinder',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='juicermixer',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='iron',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='hotplate',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='hometheater',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='attachakki',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.AddField(
            model_name='aircooler',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
    ]
