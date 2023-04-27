from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.TextField()
    notes = models.TextField()
    image = models.ImageField(blank=True, upload_to='user_property_images')
    price_select = [
        ('1', 'Within budget'),
        ('0', 'Overbudget')
    ]
    price = models.CharField(max_length=255, choices=price_select)
    
    building_age_select = [
        ('1', 'Less than 5 years'),
        ('0.5', 'Less than 10 years'),
        ('0', 'More than 10 years')
    ]
    building_age = models.CharField(max_length=255, choices=building_age_select)

    building_codes_select = [
        ('1', 'Yes'),
        ('0.5', 'Unsure'),
        ('0', 'No')
    ]
    building_codes = models.CharField(max_length=255, choices=building_codes_select)
    
    fault_line_select = [
        ('1', 'No'),
        ('0.5', 'Less than 1 kilometer away from a fault line'),
        ('0', 'Less than 5 meters away from or directly on top of a fault line')
    ]
    fault_line = models.CharField(max_length=255, choices=fault_line_select)
    
    retrofitted_select = [
        ('1', "Yes/Doesn't need retrofitting at present"),
        ('0.5', 'Unsure'),
        ('0', 'Needs to undergo retrofitting')
    ]
    retrofitted = models.CharField(max_length=255, choices=retrofitted_select)

    foundation_issues_select = [
        ('1', 'No issues/Resolved issues'),
        ('0.5', 'Issues present, unsure if resolve'),
        ('0', 'Issues present and unresolve')
    ]
    foundation_issues = models.CharField(max_length=255, choices=foundation_issues_select)

    soil_select = [
        ('1', 'Firm soil'),
        ('0.5', 'Unsure'),
        ('0', 'Loose soil')
    ]
    soil = models.CharField(max_length=255, choices=soil_select)

    building_height_select = [
        ('1', 'Lowrise (1 to 4 storeys)'),
        ('0.5', 'Midrise (5 to 15 storeys)'),
        ('0', 'Highrise (at least 16 storeys or 48 meters high)')
    ]
    building_height = models.CharField(max_length=255, choices=building_height_select)

    building_insurance_select = [
        ('1', 'Insured'),
        ('0.5', 'Incomplete insurance (e.g. has fire insurance but no earthquake insurance)'),
        ('0', 'No')
    ]
    building_insurance = models.CharField(max_length=255, choices=building_insurance_select)

    disaster_history_select = [
        ('1', 'It withstood the disaster and did not need to undergo repairs'),
        ('0.5', 'The building withstood some minor damage but it has been properly repaires since then'),
        ('0', 'There was grave damage and it has not been properly repaired')
    ]
    disaster_history = models.CharField(max_length=255, choices=disaster_history_select)

    fire_exits_select = [
        ('1', 'Fully-functional'),
        ('0.5', 'Signs of aging and needs upkeep but no worrisome'),
        ('0', 'Completely impassable, worrisome decline')
    ]
    fire_exits = models.CharField(max_length=255, choices=fire_exits_select)

    gas_valve_select = [
        ('1', 'Fully-functional'),
        ('0', 'Faulty')
    ]
    gas_valve = models.CharField(max_length=255, choices=gas_valve_select)

    evacuation_zone_select = [
        ('1', 'Nearby'),
        ('0.5', 'Not too far'),
        ('0', 'Far away')
    ]
    evacuation_zone = models.CharField(max_length=255, choices=evacuation_zone_select)

    essential_institutions_select = [
        ('1', 'Nearby'),
        ('0.5', 'Not too far'),
        ('0', 'Far away')
    ]
    essential_institutions = models.CharField(max_length=255, choices=essential_institutions_select)
    
    hospital = models.BooleanField(default=False)
    police_station = models.BooleanField(default=False)
    fire_station = models.BooleanField(default=False)
    school = models.BooleanField(default=False)
    workplace = models.BooleanField(default=False)
    grocery_or_market = models.BooleanField(default=False)
    laundromat = models.BooleanField(default=False)
    water_filling_station = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    mall = models.BooleanField(default=False)
    bills_payment_center = models.BooleanField(default=False)
    transport_terminal = models.BooleanField(default=False)
    gas_station_terminal = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    other_text = models.CharField(max_length=255, blank=True)

    safety = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    convenience = models.IntegerField(default=0)
    total_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name