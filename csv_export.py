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


class CsvBuilder(object):

    def __init__(self):

        self.headers = []

        self.rows = []

    def register_column(self, col):
        if str(col) not in self.headers:
            self.headers.append(str(col))

    def add_record_as_row(self, record):

        for key in record.keys():
            self.register_column(key)

        row = []

        for col in self.headers:
            row.append(str(record[col]))

        self.rows.append(row)

    def generate_csv(self):

        all_rows = []

        all_rows.append(','.join(self.headers))

        for row in self.rows:
            all_rows.append(','.join(row))

        return '\n'.join(all_rows)


for filename in files:
    csv = CsvBuilder()

    with open(filename, 'r') as f:
        jdata = f.read()

    data = json.loads(jdata)

    start = timestamp_to_datetime(data[0]['@timestamp'])

    for rec in data:
        row_data = {}
        for key in rec.keys():
            if type(rec[key]) is dict:
                if 'x' in rec[key].keys():
                    row_data[key+'.x'] = str(rec[key]['x'])
                    row_data[key+'.y'] = str(rec[key]['y'])
                    row_data[key+'.z'] = str(rec[key]['z'])

        csv.add_record_as_row(row_data)

    newfilename = filename.replace('json', 'csv')

    with open(newfilename, 'w') as of:
        of.write(csv.generate_csv())

#    print('File %s starts at %s and ends at %s' % (
#        filename,
#        start.strftime('%I:%M %p UTC'),
#        end.strftime('%I:%M %p UTC')
#    ))
