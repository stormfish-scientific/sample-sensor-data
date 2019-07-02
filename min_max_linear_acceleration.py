import glob
import json
import dateutil.parser
from pprint import pprint


def find_min_value(data, field, sub_field):

    # Get the value of the first record
    # and use that to start our analysis
    min_value = data[0][field][sub_field]

    # Loop through all the records.
    for record in data:

        # Get value from this record
        test_value = record[field][sub_field]

        if test_value < min_value:
            # Assign the test value as our new min value
            min_value = test_value

    # Return the min_value
    return min_value


if __name__ == '__main__':

    files = glob.glob('./export-*.json')

    files.sort()

    for filename in files:
        with open(filename, 'r') as f:
            jdata = f.read()

        data = json.loads(jdata)

        start = dateutil.parser.parse(data[0]['@timestamp'])
        end = dateutil.parser.parse(data[-1]['@timestamp'])

        min_gravity_z = find_min_value(data, 'gravity', 'z')

        print('File %s starts at %s and ends at %s' % (
            filename,
            start.strftime('%I:%M %p UTC'),
            end.strftime('%I:%M %p UTC')
        ))

        print('  The min gravity.z value found is %f' % min_gravity_z)
