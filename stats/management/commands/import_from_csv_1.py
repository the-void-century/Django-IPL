import csv
from django.core.management.base import BaseCommand
from stats.models import Deliveries,Matches  # Replace 'YourModel' with the actual model you want to import to
from django.db import transaction

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    
    def import_matches(self):
        name=self.csv_file.split('/')
        name=name[-1]
        if name=="deliveries.csv":
            self.delivery=True
        else:
            self.match=True
        try:
            with transaction.atomic():
                with open(self.csv_file, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if self.delivery:
                            row['match_id']=Matches.objects.get(id=row['match_id'])
                            instance, created =Deliveries.objects.get_or_create(**row)
                            if created:
                                instance.save()
                        elif self.match:
                            instance, created =Matches.objects.get_or_create(**row)
                            if created:
                                instance.save()
        except Exception as e:
            self.match=False
            self.delivery=False
            self.stdout.write(self.style.ERROR(e))


    def handle(self, *args, **options):
        self.match=False
        self.delivery=False
        self.csv_file = options['csv_file']
        self.import_matches()
        if self.match:
            self.stdout.write(self.style.SUCCESS('CSV import from matches completed'))
        if self.delivery:
            self.stdout.write(self.style.SUCCESS('CSV import from deliveries completed'))
