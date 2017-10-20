import csv
import datetime
import matplotlib.pyplot as plt

def load_data_objects (filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            object = {
                'StateCode' : row['StateCode'],
                'Division' : row['Division'],
                'YearMonth' : row['YearMonth'],
                'PCP' : row['PCP'],
                'TAVG' : row['TAVG']
            }
            data.append(object)

    return data

def load_data_objects_into_map (filename):
    map = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_division = row['Division']
            if (row_division not in map):
                data = []
                map[row_division] = data

            data = map[row_division]

            object = {
                'StateCode' : int(row['StateCode']),
                'Division' : int(row['Division']),
                'YearMonth' : convert_yearmonth_to_date(row['YearMonth']),
                'PCP' : float(row['PCP']),
                'TAVG' : float(row['TAVG'])
            }

            data.append(object)

    return map
# Convert string of form yyyymm into a datetime object
def convert_yearmonth_to_date (ym):
    # 201002
    str_date = str(ym)
    str_yyyy = str_date[0:4]
    str_mm = str_date[4:6]
    d = datetime.datetime(int(str_yyyy), int(str_mm), 1)
    return d

def plot_tavg(array_YEARMONTH, array_TAVG):
    plt.plot(array_YEARMONTH, array_TAVG)
    plt.title('Average Temperature')
    plt.show()

# Extract attribute from dictionary as an array
def create_attribute_array (data, attribute):
    a = []
    for x in data:
        a.append( x[attribute] )
    return a

def plot_division (division_data):

    array__DIVISION = create_attribute_array(division_data, 'Division')
    array_YEARMONTH = create_attribute_array(division_data, 'YearMonth')
    array_TAVG = create_attribute_array(division_data, 'TAVG')
    array_PCP = create_attribute_array(division_data, 'PCP')

    plt.subplot(2, 1, 1)
    plt.plot(array_YEARMONTH, array_TAVG, 'ko-')
    plt.title('Division ' + str(array__DIVISION[0]))
    plt.ylabel('TAVG (F)')

    plt.subplot(2, 1, 2)
    plt.plot(array_YEARMONTH, array_PCP, 'r.-')
    plt.xlabel('array_YEARMONTH')
    plt.ylabel('PCP')

    plt.show()

filename = "nystate_climate_indices_2010_2017.csv"
data1=load_data_objects(filename)
print(data1)

map=load_data_objects_into_map(filename)
print(map)

data_5 = map['5']  # to get the 5th division
arr_date = create_attribute_array(data_5, 'YearMonth')
arr_tavg = create_attribute_array(data_5, 'TAVG')
arr_pcp = create_attribute_array(data_5, 'PCP')

plot_tavg(arr_date, arr_tavg)

plot_division(data_5)