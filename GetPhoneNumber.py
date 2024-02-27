import phonenumbers
from phonenumbers import carrier, geocoder
typenumber = input("Enter you phone number: \n")
number = phonenumbers.parse(typenumber)
print(geocoder.description_for_number(number,'en'))
print(carrier.name_for_number(number,'en'))