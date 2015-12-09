import requests
import json
from pprint import pprint

# Read my personal token from a file 
with open("token.txt",'r') as f:
	TOKEN_NOAA = f.read()


'''
# url: http://www.ncdc.noaa.gov/cdo-web/api/v2/{endpoint}
endpoints:
/datasets 	A dataset is the primary grouping for data at NCDC.
/datacategories 	A data category is a general type of data used to group similar data types.
/datatypes 	A data type is a specific type of data that is often unique to a dataset.
/locationcategories 	A location category is a grouping of similar locations.
/locations 	A location is a geopolitical entity.
/stations 	A station is a any weather observing platform where data is recorded.
/data 	A datum is an observed value along with any ancillary attributes at a specific place and time.

'''
# Jackson, Wy - 484910
JACKSON = 'COOP:484910'
# San Dieg, CA - 047740
#url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
#url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/stations/"
#url = url+JACKSON
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/stations/COOP:047740"#&COOP:484910"
headers = {'token':TOKEN_NOAA}
response = requests.get(url, headers=headers) 
data = response.json()
import pdb; pdb.set_trace()

for i in range(len(data['results'])):

    if data['results'][i]['name'].find('CA US'):
        pprint(data)