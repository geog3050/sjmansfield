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
# Problem 1 (10 Points)
#
# This function reads all the feature classes in a workspace (folder or geodatabase) and
# prints the name of each feature class and the geometry type of that feature class in the following format:
# 'states is a point feature class'

###################################################################### 
def printFeatureClassNames(workspace):

    try:
        #importing needed systems
        import arcpy
        import os
        workspace = arcpy.env.workspace = input("Enter the workspace containing your data")
        arypy.overwriteOutput = True

        # for loop to read the feature classes
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            descObject = arcpy.Describe(fc)
            if descObject.shapeType == 'Polygon':
                print(fc, "is a polygon feature class")
            elif descObject.shapeType == 'Point Feature':
                print (fc, "is a point feature class")
            elif descObject.shapeType == 'Line':
                print (fc, "is a line feature class")
    except IOError:
        print("Please enter a valid workspace...")



        pass
    

###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the attribute names in a feature class or shape file and
# prints the name of each attribute name and its type (e.g., integer, float, double)
# only if it is a numerical type

###################################################################### 
def printNumericalFieldNames(inputFc, workspace):

    try:
        # importing needed systems
        import arcpy
        import os
        inputFc = input("Enter the feature class you would like to learn about")
        workspace = arcpy.env.workspace = input("Enter a valid workspace with your data")

        #loop to read the name and type of the attribute

        for attribute in inputFc:
            if attribute == "Integer":
                print(attibute, "is an integer")
            elif attribute == "Float":
                print(attribute, "is a float")
            elif attribute == "Double":
                print(attribute, "is a double")
            else:

    except IOError:
        print("Please enter a valid workspace")
        
    pass

###################################################################### 
# Problem 3 (30 Points)
#
# Given a geodatabase with feature classes, and shape type (point, line or polygon) and an output geodatabase:
# this function creates a new geodatabase and copying only the feature classes with the given shape type into the new geodatabase

###################################################################### 
def exportFeatureClassesByShapeType(input_geodatabase, shapeType, output_geodatabase):
    try:
        # User inputs
        input_geodatabase = input("Enter your database you would like to copy from")
        shapeType = input("Enter the shape type you would like to copy")
        output_geodatabase = input("Enter the new geodatabase you would like to copy to")
        # creating database
        dir_path = os.path.dirname(os.path.realpath(input_gdb))
        arcpy.CreateFileGDB_management(dir_path, 'output_geodatabase')
        # copying over
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            if fc == shapeType:
                arcpy.CopyFeatures_management(fc, output_database)
            else:
    except IOError:
        print("Please enter a valid geodatabase to start from...")


    pass

###################################################################### 
# Problem 4 (40 Points)
#
# Given an input feature class or a shape file and a table in a geodatabase or a folder workspace,
# join the table to the feature class using one-to-one and export to a new feature class.
# Print the results of the joined output to show how many records matched and unmatched in the join operation. 

###################################################################### 
def exportAttributeJoin(inputFc, idFieldInputFc, inputTable, idFieldTable, workspace):
    
    try:

        #import needed systems
        
        import arcpy
        import os
        # create user inputs
        
        inputFc = input("Please enter the feature class you would like to join")
        idFieldInputFc = input("Please enter the the ID of the field you would like to join")
        inputTable = input("Please enter the table you would like to join")
        idFieldTable = input("Please enter the ID of the table you would like to join")
        workspace = arcpy.env.workspace = input("Enter a valid workspace with your data")
        # code to enact the join

        new_joined_table = arcpy.management.AddJoin(inputFc, idFieldInputFc, inputTable, idFieldTable)

        #printing results

        for fc in new_joined_table:
            if fc is in inputTable and new_joined_table:
                result = fc
            print(result)

    except IOError:
        print("Please enter valid inputs for your files...")
        pass


######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
