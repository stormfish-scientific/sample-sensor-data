import glob
import json
import dateutil.parser
from pprint import pprint

files = glob.glob('./export-*.json')

files.sort()

for filename in files:
    with open(filename, 'r') as f:
        jdata = f.read()

    data = json.loads(jdata)

    start = dateutil.parser.parse(data[0]['@timestamp'])
    end = dateutil.parser.parse(data[-1]['@timestamp'])

    print('File %s starts at %s and ends at %s' % (
        filename,
        start.strftime('%I:%M %p UTC'),
        end.strftime('%I:%M %p UTC')
    ))
