import glob
import json
from datetime import datetime

from pprint import pprint


# Get the timestamp
def timestamp_to_datetime(timestamp):
    # Make a copy so that we don't modify the original
    timestamp_string = str(timestamp)
    timestamp_string = timestamp_string.replace('Z', '000')

    return datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%S.%f')


files = glob.glob('./export-*.json')

files.sort()

for filename in files:
    with open(filename, 'r') as f:
        jdata = f.read()

    data = json.loads(jdata)

    start = timestamp_to_datetime(data[0]['@timestamp'])

    pprint({'original': data[0]['@timestamp'],
            'datetime': start})


#    print('File %s starts at %s and ends at %s' % (
#        filename,
#        start.strftime('%I:%M %p UTC'),
#        end.strftime('%I:%M %p UTC')
#    ))
