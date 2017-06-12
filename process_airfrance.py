# coding='utf-8'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Import the modules
import json
import csv
import pandas as pd
from bs4 import BeautifulSoup




def process_html(doc):

    results_data = []

    with open('airfrance_cities.json') as data_file:
        cities = json.load(data_file)["Cities"]

    # print len(cities)

    soup = BeautifulSoup(open(doc + ".html"), 'html.parser')

    # all_tables = soup.find_all('table')
    # all_tr = soup.find_all('tr')
    all_results_details = soup.find_all("tr", class_="results-list-details")

    print "Results length:", len(all_results_details)

    for index, detail in enumerate(all_results_details):

        # print index

        # "un seul troncon"
        troncon = list(all_results_details[index].contents[1].tbody.children)[1].td.h2.string.strip()
        # print troncon


        ## Depart

        # Aeroport de depart
        departure_airport_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[3])[1])[3].stripped_strings)[0].strip()
        departure_airport_code = list(list(list(list(all_results_details[index].contents[1].tbody.children)[3])[1])[3].stripped_strings)[1][1:4]
        print departure_airport_code

        # Ville de depart
        departure_city_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[1])[3].stripped_strings)[0].strip()
        departure_city_code = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[1])[3].stripped_strings)[1][1:4]

        # Find lat/lon
        departure_city_obj = next(city for city in cities if city["Code"] == departure_city_code)
        departure_city_longitude = departure_city_obj["Lon"]
        departure_city_latitude = departure_city_obj["Lat"]

        # Pays de depart
        departure_country_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[7])[1])[3].stripped_strings)[0].strip()
        departure_country_code = list(list(list(list(all_results_details[index].contents[1].tbody.children)[7])[1])[3].stripped_strings)[1][1:3]


        ## Arrivee

        # Aeroport d'arrivee
        arrival_airport_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[3])[3])[3].stripped_strings)[0].strip()
        arrival_airport_code = list(list(list(list(all_results_details[index].contents[1].tbody.children)[3])[3])[3].stripped_strings)[1][1:4]
        # print arrival_airport_name, arrival_airport_code[1:4]

        # Ville d'arrivee
        arrival_city_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[3])[3].stripped_strings)[0].strip()
        arrival_city_code = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[3])[3].stripped_strings)[1][1:4]

        # Find lat/lon
        arrival_city_obj = next(city for city in cities if city["Code"] == arrival_city_code)
        arrival_city_longitude = arrival_city_obj["Lon"]
        arrival_city_latitude = arrival_city_obj["Lat"]

        # Pays d'arrivee
        arrival_country_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[7])[3])[3].stripped_strings)[0].strip()
        arrival_country_code = list(list(list(list(all_results_details[index].contents[1].tbody.children)[7])[3])[3].stripped_strings)[1][1:3]


        # Compagnie aerienne
        airline_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[3])[5])[3].stripped_strings)[0].strip()
        try:
            airline_assured_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[3])[5])[3].stripped_strings)[2].strip()
        except:
            airline_assured_name = None


        # Escales
        stopover = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[5])[3].stripped_strings)[0]
        if stopover == "Non-stop":
            stopover_count = 0
            stopover_airport_name = ""
            stopover_airport_code = ""
            stopover_city_name = ""
            stopover_city_code = ""
            stopover_city_longitude = ""
            stopover_city_latitude = ""
            stopover_country = ""
        else:
            print "/// STOPOVER"
            stopover_count = int(stopover[0:1])
            stopover_city = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[5])[3].stripped_strings)[1].split("(")
            stopover_airport_name = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[5])[3].stripped_strings)[2].strip()
            stopover_airport_code = stopover_city[1].split(")")[0]
            stopover_city_name = stopover_city[0].strip()
            # Find lat/lon
            stopover_city_obj = next(city for city in cities if city["Name"] == stopover_city_name)
            print stopover_city_obj
            stopover_city_longitude = stopover_city_obj["Lon"]
            stopover_city_latitude = stopover_city_obj["Lat"]
            stopover_city_code = stopover_city_obj["Code"]
            stopover_country = list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[5])[3].stripped_strings)[3].strip()
            print departure_city_name, arrival_city_name, " / Stopover: ", stopover_city_name, stopover_city_code, stopover_airport_code

            # don't manage 2 stopovers (yet?)
            if stopover_count == 2:
                print "===2 STOPOVERS===", index, list(list(list(list(all_results_details[index].contents[1].tbody.children)[5])[5])[3].stripped_strings)

        # Distance
        distance = list(list(list(list(all_results_details[index].contents[1].tbody.children)[7])[5])[3].stripped_strings)[0].split(" km")[0].replace(",","")

        # Type (for d3)
        type = "LineString"

        # departure_airport_name,departure_airport_code,departure_city_name,departure_city_code,departure_city_longitude,departure_city_latitude,departure_country_name,departure_country_code,arrival_airport_name,arrival_airport_code,arrival_city_name,arrival_city_code,arrival_city_longitude,arrival_city_latitude,arrival_country_name,arrival_country_code,airline_name,airline_assured_name,stopover_count,stopover_city_name,stopover_city_code,stopover_city_longitude,stopover_city_latitude,stopover_airport_name,stopover_airport_code,stopover_country,distance,type
        results_data.append([ \
            # troncon, \
            departure_airport_name, \
            departure_airport_code, \
            departure_city_name, \
            departure_city_code, \
            departure_city_longitude, \
            departure_city_latitude, \
            departure_country_name, \
            departure_country_code, \
            arrival_airport_name, \
            arrival_airport_code, \
            arrival_city_name, \
            arrival_city_code, \
            arrival_city_longitude, \
            arrival_city_latitude, \
            arrival_country_name, \
            arrival_country_code, \
            airline_name, \
            airline_assured_name, \
            stopover_count, \
            stopover_city_name, \
            stopover_city_code, \
            stopover_city_longitude, \
            stopover_city_latitude, \
            stopover_airport_name, \
            stopover_airport_code, \
            stopover_country, \
            distance, \
            type \
        ])

    with open("airfrance.csv", 'a') as f:
        wr = csv.writer(f, delimiter=',', lineterminator='\n')
        wr.writerows(results_data)


"""
main()
"""
if __name__ == '__main__':

    # removed "&lrm;"

    # html_docs = ["airfrance_paris_1", "airfrance_paris_2", "airfrance_paris_3", "airfrance_amsterdam_1", "airfrance_amsterdam_2", "airfrance_amsterdam_3"];
    #
    # for doc in html_docs:
    #     process_html(doc)


    html_doc = "airfrance_rotterdam_1"
    process_html(html_doc)
