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
    return(["Sam Mansfield", "sjmansfield"])

###################################################################### 
# Problem 1 (20 points)
# 
# Given an input point feature class (e.g., facilities or hospitals) and a polyline feature class, i.e., bike_routes:
# Calculate the distance of each facility to the closest bike route and append the value to a new field.
#        
###################################################################### 
def calculateDistanceFromPointsToPolylines(input_geodatabase, fcPoint, fcPolyline):

    try:
        #import needed programs and create workspace

        import arcpy
        import os
        arcpy.env.workspace = input('Enter a valid workspace')

        #create user inputs

        input_geodatabase = input('Please enter a GDB')
        fcPoint = input('Enter the point layer where you would like to start')
        fcPolyline = input('Enter the polygone layer you would like to use')
        NewFieldTable = input('Enter the table you would like to the distance field to go to')

        # adding a new field

        arcpy.management.AddField("NewFieldTable", "NewDist", "DOUBLE")

        # distance function

        distance = arcpy.analysis.PointDistance(fcPoint, fcPolyline, NewFieldTable)

        # appending

        arcpy.management.Append(distance, NewDist)
        pass

    except IOError:
        print('Please enter a valid workspace!')
        

######################################################################
# Problem 2 (30 points)
# 
# Given an input point feature class, i.e., facilities, with a field name (FACILITY) and a value ('NURSING HOME'), and a polygon feature class, i.e., block_groups:
# Count the number of the given type of point features (NURSING HOME) within each polygon and append the counts as a new field in the polygon feature class
#
######################################################################
def countPointsByTypeWithinPolygon(input_geodatabase, fcPoint, pointFieldName, pointFieldValue, fcPolygon):

    try:

        # Importing moduals and workspace

        import arcpy
        import os
        arcpy.env.workspace = input('Enter a valid workspace')

        # creating user inputs

        input_geodatabase = input('Please enter a valid GDB')
        fcPoint = input('Please enter the point feature class you would like to use')
        pointFieldName = input('Please enter the field name of the point feature class you selected')
        pointFieldValue = input('Please enter the value type of the point feature class you selected')
        fcPolygon = input('Please enter the polygon layer you would like to use')

        # creating a new field

        arcpy.management.AddField(fcPolygon, "CountPoints", "DOUBLE")

        # summarizing within function

        pointswithin = arcpy.analysis.SummarizeWithin(fcPoint, fcPolygon, "Points_within")

        # appending 

        arcpy.management.Append(pointswithin, "CountPoints"

        
    pass

######################################################################
# Problem 3 (50 points)
# 
# Given a polygon feature class, i.e., block_groups, and a point feature class, i.e., facilities,
# with a field name within point feature class that can distinguish categories of points (i.e., FACILITY);
# count the number of points for every type of point features (NURSING HOME, LIBRARY, HEALTH CENTER, etc.) within each polygon and
# append the counts to a new field with an abbreviation of the feature type (e.g., nursinghome, healthcenter) into the polygon feature class 

# HINT: If you find an easier solution to the problem than the steps below, feel free to implement.
# Below steps are not necessarily explaining all the code parts, but rather a logical workflow for you to get started.
# Therefore, you may have to write more code in between these steps.

# 1- Extract all distinct values of the attribute (e.g., FACILITY) from the point feature class and save it into a list
# 2- Go through the list of values:
#    a) Generate a shortened name for the point type using the value in the list by removing the white spaces and taking the first 13 characters of the values.
#    b) Create a field in polygon feature class using the shortened name of the point type value.
#    c) Perform a spatial join between polygon features and point features using the specific point type value on the attribute (e.g., FACILITY)
#    d) Join the counts back to the original polygon feature class, then calculate the field for the point type with the value of using the join count field.
#    e) Delete uncessary files and the fields that you generated through the process, including the spatial join outputs.  
######################################################################
def countCategoricalPointTypesWithinPolygons(fcPoint, pointFieldName, fcPolygon, workspace):

    try:
        
        # inport needed os

        import arcpy
        import os
        arcpy.env.workspace = workspace

        # user inputs

        fcpoint = input('Enter which point featureclass you would like to use')
        pointFieldName = input('What is the field name you would like to use?')
        fcPolygon = input('Enter a valid polygon to use')
        workspace = input('Please enter a valid workspace')

        # add field

        newField = arcpy.management.AddField('fcPolygon', 'pointFieldName' + count, 'DOUBLE')

        # finding the count of points

        count_of_points = arcpy.analysis.SummerizeWithin('fcPolygon', 'fcpoint', "Count_of_points_fc)

        # appending the data back to the field
        # i think this was more simple, but I could be wrong. I am trying to get all of my assignments in so that I can have a solid final project                                                 
                                               
        arcpy.management.Append(count_of_points, newField)

    except:
        print('Please enter valid data')

    

    
    pass

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
