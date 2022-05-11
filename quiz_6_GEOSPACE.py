def calculatePercentAreaOfPolygonAinPolygonB(input_geodatabase, fcPolygon1, fcPolygon2, idFieldPolygonB):

    try:

        #importing

        import arcpy
        import os

        # setting workspace

        arcpy.env.workspace = 'input_geodatabase'
        arcpy.env.overwriteOutput = True

        # user inputs

        input_geodatabase = input('Please enter a valid GDB')
        fcPolygon1 = input('Enter the first polygon you would like to use')
        fcPolygon2 = input('Enter the second polygon you would like to use')
        idFieldPolygonB = input('Enter the field you would like to us')

        # adding field

        arcpy.AddField_management(fcPolygon1, "areasqm", "DOUBLE")

        # intersecting layers

        intersected_poly = arcpy.analysis.Intersect([fcPolygon1, fcPolygon2], "intersected_layer")

        #calculating area

        new_area = arcpy.CalculateGeometryAttributes_management(intersected_poly, [["areasqm", "AREA"]], "MILES_US", "SQUARE_MILES_US")

        # dictionary

        dict = {}

        # search cursor

        new_value = with arcpy.da.SearchCursor(intersected_poly, idFieldPolygonB) as cursor:
            for row in cursor:
                if row[7] = idFieldPolygonB:
                    dict.Update(row[7])
                else:
                    pass

        # new field

        arcpy.AddField_management(fcPolygon1, "Percent_area", "DOUBLE")

        # update cursor

        with arcpy.da.UpdateCursor(fcPolygon1, "Percent_area") as cursor:
            row == new_value

            cursor.updateRow(cursor)

    except:
        print("These inputs were not valid!)
            
            

    
