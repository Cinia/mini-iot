#!/bin/python

from flask import Flask
from flask import render_template
from flask import jsonify
from influxdb import InfluxDBClient
import re

app = Flask(__name__)

hostName = "77.95.246.253"
client = InfluxDBClient(hostName, 8086, '', '', 'mini-iot')

def get_tags_for_series(series_name, tag_name):
    found_tags = []
    resultset = client.query("show series")
    for serie in list(resultset.get_points()):
        if serie['key'].startswith(series_name):
            match = re.search("[-a-zA-Z]+,([a-zA-Z]+)=([a-zA-Z]+)", serie['key'])
            if match == None:
                print("FAIL: could not parse tags from serie: " + serie['key'])
            else:
                if tag_name == match.group(1):
                  #  print(match.group(2))
                    found_tags.append(match.group(2))
                else:
                    print("Found tag '" + match.group(1) + "=" + match.group(2) + "' which is skipped")
        #else: 
                #print("Did not match :" + serie['key'])
    return found_tags

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/api/temperature")
def get_available_tags():
    tag_list = get_tags_for_series("temperature", "source")
    return jsonify({'tags': tag_list})


@app.route("/api/temperature/<source>")
def get_temperature(source):
    #client = InfluxDBClient(hostName, 8086, '', '', 'mini-iot')
    
    #tags = get_tags_for_series("temperature", "source")    
    
    query = "select time, mean(value) as value from temperature where source = '" + source + "' and time > now() - 1d group by time(30m);"
    print(query)
    result = client.query(query)
    return jsonify(list(result.get_points()))

if __name__ == "__main__":
    app.run()