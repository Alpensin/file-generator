import csv
data = csv.reader(open(r'C:\TEMP\mo_50.csv'), delimiter = ',')
with open('csv2kml.kml', 'w') as f:
    f.write('''<?xml version='1.0' encoding='UTF-8'?><kml xmlns='http://earth.google.com/kml/2.2'><Document><name>mo_50_route.kml</name><Style id="1"><IconStyle><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/paddle/blu-blank-lv.png</href></Icon></IconStyle></Style>''')
    for row in data:
        f.write(f"<Placemark><styleUrl>#1</styleUrl><Point><coordinates>{row[0]},{row[1]}</coordinates></Point></Placemark>")     
    f.write("</Document></kml>")