import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LittleLemon.settings')
django.setup()

# Now you can import your Django components
from LittleLemon.urls import router  # Adjust this import path to where your router is defined

# Your script to list URLs
for urlpattern in router.urls:
    print(urlpattern.pattern)