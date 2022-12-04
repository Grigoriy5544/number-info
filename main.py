import phonenumbers
from phonenumbers import carrier, geocoder, timezone

number = input('Введите номер телефона: ')
phoneNumber = phonenumbers.parse(number)

Carrier = carrier.name_for_number(phoneNumber, 'ru')
  
Region = geocoder.description_for_number(phoneNumber, 'ru')
timeZone = timezone.time_zones_for_number(phoneNumber)

valid = phonenumbers.is_valid_number(phoneNumber)

print(valid)
if valid:
    print(Carrier)
    print(Region)
    print(timeZone)