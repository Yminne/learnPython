import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

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

# Extract attribute from dictionary as an array
def create_attribute_array (data, attribute):
    a = []
    for x in data:
        a.append( x[attribute] )
    return a

# Calculate the mean of an array
def mean(b):
    return sum(b) / float(len(b))

def perform_analysis(data_map):
    stats = []
    for division in data_map:
        division_data = data_map[division]
        array_TAVG = create_attribute_array(division_data, 'TAVG')
        array_PCP = create_attribute_array(division_data, 'PCP')

        # Calcualte stats for each station
        max_TAVG = max(array_TAVG)
        min_TAVG = min(array_TAVG)
        mean_PCP = mean(array_PCP)

        station_stats = {
            "station" : int(division),
            "max_TAVG" : max_TAVG,
            "min_TAVG" : min_TAVG,
            "mean_PCP" : mean_PCP
        }
        stats.append(station_stats)
    print(stats)
    return stats

def plot_min_max (station_stats):
    array_STATION = create_attribute_array(station_stats, 'station')
    array_MIN_TAVG = create_attribute_array(station_stats, 'min_TAVG')
    array_MAX_TAVG = create_attribute_array(station_stats, 'max_TAVG')
    array_MEAN_PCP = create_attribute_array(station_stats, 'mean_PCP')

    N = len(array_STATION)
    ind = np.arange(N)  # the x locations for the groups

    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, array_MIN_TAVG, width, color='b')
    rects2 = ax.bar(ind + width, array_MAX_TAVG, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average Temperature (F)')
    ax.set_title('Min and Max Temperature by Station')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(array_STATION)
    ax.legend((rects1[0], rects2[0]), ('Min', 'Max'))
    plt.show()


filename = "nystate_climate_indices_2010_2017.csv"
map=load_data_objects_into_map(filename)
#print(map)
stats1=perform_analysis(map)
plot_min_max(stats1)