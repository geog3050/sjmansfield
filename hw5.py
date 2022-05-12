###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Sam Mansfield", "smansfield"])

###################################################################### 
# Problem 1 (30 Points)
#
# Given a polygon feature class in a geodatabase, a count attribute of the feature class(e.g., population, disease count):
# this function calculates and appends a new density column to the input feature class in a geodatabase.

# Given any polygon feature class in the geodatabase and a count variable:
# - Calculate the area of each polygon in square miles and append to a new column
# - Create a field (e.g., density_sqm) and calculate the density of the selected count variable
#   using the area of each polygon and its count variable(e.g., population) 
# 
# 1- Check whether the input variables are correct(e.g., the shape type, attribute name)
# 2- Make sure overwrite is enabled if the field name already exists.
# 3- Identify the input coordinate systems unit of measurement (e.g., meters, feet) for an accurate area calculation and conversion
# 4- Give a warning message if the projection is a geographic projection(e.g., WGS84, NAD83).
#    Remember that area calculations are not accurate in geographic coordinate systems. 
# 
###################################################################### 
def calculateDensity(fcpolygon, attribute,geodatabase = "assignment2.gdb"):

    try:

        #import

        import arcpy
        import os
        # user inputs

        fcpolygon = input("Please enter the polygon you would like to use")
        attribute = input("please choose an attribute of the feature class (count)")

        # creating a new field

        arcpy.management.AddField(fcpolygon, "density_sqm", "LONG")

        # calculating density

        binsize = "1 Kilometers"
        neighborhoodSize = "2 Kilometers"

        density = arcpy.geoanalytics.CalculateDensity(fcpolygon, "Density_out", "SQUARE", binsize, "UNIFORM", neighborhoodSize, attribute)

        # putting it in the field

        arcpy.management.CalculateField(fcpolygon, "density_sqm", "!density!")

    except:
        print("Check to make sure your inputs are correct!")
        

    


###################################################################### 
# Problem 2 (40 Points)
# 
# Given a line feature class (e.g.,river_network.shp) and a polygon feature class (e.g.,states.shp) in a geodatabase, 
# id or name field that could uniquely identify a feature in the polygon feature class
# and the value of the id field to select a polygon (e.g., Iowa) for using as a clip feature:
# this function clips the linear feature class by the selected polygon boundary,
# and then calculates and returns the total length of the line features (e.g., rivers) in miles for the selected polygon.
# 
# 1- Check whether the input variables are correct (e.g., the shape types and the name or id of the selected polygon)
# 2- Transform the projection of one to other if the line and polygon shapefiles have different projections
# 3- Identify the input coordinate systems unit of measurement (e.g., meters, feet) for an accurate distance calculation and conversion
#        
###################################################################### 
def estimateTotalLineLengthInPolygons(fcLine, fcClipPolygon, polygonIDFieldName, clipPolygonID, geodatabase = "assignment2.gdb"):

    try:

        # importing

        import arcpy
        import os

        # user inputs

        fcline = input("Enter a line feature class")
        fcClipPolygon = input("Choose a polygon feature class")
        polygonIDFieldName = input("Choose a field within your selected polygon")
        clipPolygonID = input("Enter the field that you would like to use a clip feature")

        # checking the projections

        descfcLine = arcpy.Describe(fcLine)
        sreffcLine = arcpy.descfcLine.spatialReference

        descPoly = arcpy.Describe(fcClipPolygon)
        srefPoly = arcpy.descPoly.spatialReference

        if sreffcLine != srefPoly:
            arcpy.Project_management(fcline, "fcline_project", srefPoly)
        else:

        # summerize within

        length_within = arcpy.analysis.SummarizeWithin(fcClipPolygon, fcline, "outfc", "KEEP_ALL", "SUM", "MILES")

    except:
        print("Are your inputs all valid?")
    

######################################################################
# Problem 3 (30 points)
# 
# Given an input point feature class, (i.e., eu_cities.shp) and a distance threshold and unit:
# Calculate the number of points within the distance threshold from each point (e.g., city),
# and append the count to a new field (attribute).
#
# 1- Identify the input coordinate systems unit of measurement (e.g., meters, feet, degrees) for an accurate distance calculation and conversion
# 2- If the coordinate system is geographic (latitude and longitude degrees) then calculate bearing (great circle) distance
#
######################################################################
def countObservationsWithinDistance(fcPoint, distance, distanceUnit, geodatabase = "assignment2.gdb"):

    try:

        # importing

        import arcpy
        import os

        #user inputs

        fcPoint = input('Please select a point feature class to use')
        distance = input('Please enter a distance threshold')
        distanceUnit = input('What unit of distance would you like to use')

        # creating a new field

        arcpy.management.AddField(fcPoint, "PointsWthn", "LONG")

        # near analysis

        for point in fcPoint:
            countwthn = arcpy.analysis.Near(fcPoint, fcPoint, distance + distanceUnit)

        # filling the field

        arcpy.management.CalculateField(fcPoint, "PointsWitn", "!countwthn!")

        
    except:
        print("Does your point class include latitude and longitude?)

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
