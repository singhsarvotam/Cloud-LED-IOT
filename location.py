# PART 1


from geopy.geocoders  import Nominatim
from geopy.distance import vincenty
import time
from random import randint
from datetime import datetime


geolocator = Nominatim()
HomeLocation = input("\n\nPlease Enter your home location : ")
location = geolocator.geocode(HomeLocation)

home_loc_cordinates = "(" + str(location.latitude) + "," +  str(location.longitude) + ")"

time.sleep(2)
print('\nHome Address :' , location.address , '\n')
print("Home Longitude : ",location.latitude,"Home Latitude", location.longitude)


curr_latitude = location.latitude - 2
#print("\n\nUpdated Location Longitude : ",curr_latitude)


cur_loc_cordinates = "(" + str(curr_latitude) + "," +  str(location.longitude) + ")"

curr_location = geolocator.reverse(str(curr_latitude) + "," + str(location.longitude))
print('\nYou are currently at : ' , curr_location.address)


print('You are ', vincenty(home_loc_cordinates, cur_loc_cordinates).miles , 'miles apart from home.\n\n')


near_home_latitude = location.latitude - 1



while curr_latitude <= near_home_latitude :
	time.sleep(1)
	curr_latitude = curr_latitude + 0.1
	cur_loc_cordinates = "(" + str(curr_latitude) + "," +  str(location.longitude) + ")"
	#print('\nYou are currently at : ' , curr_location.address)
	print(' current location : ' , "(", str(curr_latitude) + "," + str(location.longitude) , ")")

time.sleep(2)

print('\n\nYou are currently at : ' , "(", str(curr_latitude) + "," + str(location.longitude) , ")")
print ('\nYou are near your home. Turing on the AC')	



print ('\n\n\n PART 2 : RPM and AIRFLOW \n')	
#Part 2
# http://www.greenheck.com/media/pdf/qdcatalog/FanFundamentals.pdf
initial_RPM = 20
initial_CFM = 1000

CFM =initial_CFM ; #setting the sir flow rate
rpm= initial_RPM ;
for num in range(1,10) :
	p = randint(50,150)
	if p > 100 :
		print ('abnormal behaviour (rpm below 100)')
		continue
	else :
		CFM_new = (p/rpm) * CFM
		CFM=CFM_new
		rpm=p
		time.sleep(1)
		tme = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print ("At " , tme ," RPM is" , p , " with airflow rate of " , round(CFM_new,2) )
		




