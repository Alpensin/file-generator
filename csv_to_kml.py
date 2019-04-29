import csv
#Input the file name."JoeDupes3_forearth"
data = csv.reader(open(r'C:\TEMP\mo_50.csv'), delimiter = ',')
#Skip the 1st header row.
#data.next()
#Open the file to be written.
with open('csv2kml.kml', 'w') as f:
#Writing the kml file.
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<kml xmlns='http://earth.google.com/kml/2.2'>\n")
    f.write("<Document>\n")
    f.write("   <name>" + 'mo_50_route' + '.kml' +"</name>\n")
    f.write('       <Style id="1"><IconStyle><scale>0.4</scale><Icon><href>http://maps.google.com/mapfiles/kml/paddle/blu-blank-lv.png</href></Icon></IconStyle></Style>')
    for row in data:
        f.write("   <Placemark>\n")
        f.write("   <styleUrl> #1</styleUrl>\n")
        # f.write("       <name>" + 'route' + "</name>\n")
        # f.write("       <description>" + ' ' + "</description>\n")
        f.write("       <Point>\n")
        f.write("           <coordinates>" + str(row[0]) + "," + row[1] + "</coordinates>\n")
        f.write("       </Point>\n")
        f.write("   </Placemark>\n")
    f.write("</Document>\n")
    f.write("</kml>\n")
