import googlemaps
import datetime
import numpy as np
import math
import pickle

file = open("../key.txt", 'r')
API_KEY = file.read().rstrip()
print API_KEY
ENABLED = False #only get 2500 requests a day, so use sparingly

def getTravelTime(origin, destination, departure_datetime):
    #sampleJson = {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'22 mins', u'value': 1339}, u'distance': {u'text': u'28.2 km', u'value': 28165}, u'duration_in_traffic': {u'text': u'24 mins', u'value': 1413}, u'status': u'OK'}]}], u'origin_addresses': [u'Minneapolis, MN, USA'], u'destination_addresses': [u'Eden Prairie, MN, USA']}
    #print sampleJson['rows'][0]['elements'][0]['duration_in_traffic']['text']
    return gmaps.distance_matrix(origin, destination, departure_time = departure_datetime)['rows'][0]['elements'][0]['duration_in_traffic']['value']

def getTravelTimes(origin, destination, departure_datatime_list):
    travelTimes = []
    now = datetime.datetime.now()
    for time in departure_datatime_list:
        toDateTime = datetime.datetime(now.year, now.month, now.day + 4, int(math.modf(time)[1]), int(60 * math.modf(time)[0]))
        travelTimes.append([toDateTime, getTravelTime(origin, destination, departure_datetime=toDateTime)])
    return travelTimes

gmaps = googlemaps.Client(key=API_KEY)
if not ENABLED:
    gmaps = None

leaveHomeTimes = np.arange(6.4,11.6,0.2)
leaveWorkTimes = np.arange(2.4 + 12, 7.6 + 12, .2)

home_address = open("../homeAddress.txt", 'r').read().rstrip()
work_address = open("../workAddress.txt", 'r').read().rstrip()

h2wFileName = "homeToWorkTravelTimes.p"
#This fills the h2w and saves data
homeToWorkTravelTimes = getTravelTimes(home_address, work_address, leaveHomeTimes)
pickle.dump( homeToWorkTravelTimes, open( h2wFileName, "wb" ) )

w2homeFileName = "workToHomeTravelTimes.p"
workToHomeTravelTimes = getTravelTimes(work_address, home_address, leaveWorkTimes)
pickle.dump( workToHomeTravelTimes, open( w2homeFileName, "wb" ) )


