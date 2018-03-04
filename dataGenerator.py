from geopy.geocoders import Nominatim
from random import * 

# userName =["Cecil Palmer","Lillian Jackson","Becky Larson","Lucy King","Flenn Ramirez","Darren Freeman","Terry Watts","Phillip Reynolds","Celina Williams","Brandie Kuhn"]

# userURL = ["https://randomuser.me/api/portraits/men/90.jpg","https://randomuser.me/api/portraits/women/3.jpg","https://randomuser.me/api/portraits/women/45.jpg","https://randomuser.me/api/portraits/women/24.jpg","https://randomuser.me/api/portraits/men/63.jpg","https://randomuser.me/api/portraits/men/53.jpg","https://randomuser.me/api/portraits/men/1.jpg","https://randomuser.me/api/portraits/men/11.jpg","https://randomuser.me/api/portraits/women/94.jpg","https://randomuser.me/api/portraits/women/14.jpg"]

flat_images = ["https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat1.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat2.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat3.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat4.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat5.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat6.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat1.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat2.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat3.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat4.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat5.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat6.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat1.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat2.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat3.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat4.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat5.jpg", "https://raw.githubusercontent.com/lewagon/flats-boilerplate/master/images/flat6.jpg"]



f = open("flatsInfo.txt", 'r')
output_file = open('flats.txt', 'w')

data = f.read().split("\n")

locator = Nominatim()
counter = 0
# print(len(data))
for i in range(0,int(len(data)+1/8)-1,2):
	address = data[i]
	date = data[i+1]
	location = locator.geocode(address+", oshawa", timeout=20)
	if location == None:
		continue
	print(location)
	user_id = randint(0,9)
	num = randint(0,17)
	output_file.write("{\"id\": %i, \"address\": \"%s\", \"date\": \"%s\", \"imageUrl\": \"%s\", \"licensed\": True,  \"lat\": \"%s\", \"lng\": \"%s\", \"user_id\": %i },\n" % (counter, address, date, flat_images[num], location.latitude, location.longitude, user_id))
	counter += 1


output_file.close()
f.close()