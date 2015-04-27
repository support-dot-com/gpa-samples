from django.db import models
import random, copy

# Create your models here.
deviceList = [
  {"id":324125,"model":"IPhone 4s","make":"Apple","os":"iOS"},
  {"id":984235,"model":"IPhone 5","make":"Apple","os":"iOS"},
  {"id":124356,"model":"HTC One","make":"HTC","os":"Android"},
  {"id":867323,"model":"Samsung Galaxy S5","make":"Samsung","os":"Android"},
  {"id":877872,"model":"Nexus 6","make":"Motorola","os":"Android"},
  {"id":453546,"model":"OnePlus One","make":"OnePlus","os":"Android"},
  {"id":767632,"model":"Eee Pad","make":"ASUS","os":"Android"},
  {"id":236245,"model":"Moto X","make":"Motorola","os":"Android"},
  {"id":886232,"model":"Thinkpad","make":"Lenovo","os":"Windows 7"},
  {"id":534253,"model":"Latitude","make":"Dell","os":"Windows 8.1"},
  {"id":753725,"model":"Pavilion","make":"HP","os":"Windows 8"},
  {"id":412653,"model":"Mac book Pro","make":"Apple","os":"OSX"},
]

def getByConsumer(consumer):
  random.seed(consumer)
  devices = copy.deepcopy(random.sample(deviceList, random.randint(1,6)))

  for device in devices:
    random.seed()
    device["battery"] = {"level":random.randint(2, 100),"charging":bool(random.getrandbits(1))}
    device["disk"] = {"used":random.randint(60, 95)}

  return devices
