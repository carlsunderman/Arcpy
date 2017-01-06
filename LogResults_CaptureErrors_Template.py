# ---------------------------------------------------------------------------
# Name: Template ArcPy Script for Writing Messages to Text File
#
# Author: Patrick McKinney, Cumberland County GIS (pmckinney@ccpa.net or pnmcartography@gmail.com)
#
# Created on: 01/06/2017
#
# Description: This is a template script for running ArcGIS geoprocessing tool(s).
# It is ideally suited for scripts that run as Windows scheduled tasks.
# The script writes success or error messages in a text file.
# You must update the path and name of the text file.
# The ArcPy geoprocessing code goes in at line 39.
#
# Disclaimer: CUMBERLAND COUNTY ASSUMES NO LIABILITY ARISING FROM USE OF THESE MAPS OR DATA. THE MAPS AND DATA ARE PROVIDED WITHOUT
# WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE.
# Furthermore, Cumberland County assumes no liability for any errors, omissions, or inaccuracies in the information provided regardless
# of the cause of such, or for any decision made, action taken, or action not taken by the user in reliance upon any maps or data provided
# herein. The user assumes the risk that the information may not be accurate.
# ---------------------------------------------------------------------------

# Import system modules
import arcpy
import os, sys, time, datetime, traceback, string

# Time stamp variables
currentTime = datetime.datetime.now()
# Date formatted as month-day-year (1-1-2017)
date1 = currentTime.strftime("%m-%d-%Y")
# Date formatted as month-day-year-hour-minute-second (1-1-2017-15-42-09)
date2 = currentTime.strftime("%Y-%m-%d-%H-%M-%S")

# Create text file for logging results of script
# Update file path with your parameters
# Each time the script runs, it creates a new text file with the date1 variable as part of the file name
# The example would be GeoprocessingReport_1-1-2017
file = r'C:\GIS\Results\GeoprocessingReport_%s.txt' % date1

# Open text file in write mode and log results of script
report = open(file,'w')

# Run geoprocessing tool.
# If there is an error with the tool, it will break and run the code within the except statement
try:
    # Get the start time of the geoprocessing tool(s)
    starttime = time.clock()

    # Put ArcPy geoprocessing code within this section

    # Get the end time of the geoprocessing tool(s)
    finishtime = time.clock()
    # Get the total time to run the geoprocessing tool(s)
    elapsedtime = finishtime - starttime

    # write result messages to log
    # delay writing results until geoprocessing tool gets the completed code
    while result.status < 4:
        time.sleep(0.2)
    # store tool result message in a variable
    resultValue = result.getMessages()
    # write the tool's message to the log file
    report.write ("completed " + str(resultValue) + "\n \n")
    # Write a more human readable message to log
    report.write("Successfully ran the geoprocessing tool in " + str(elapsedtime) + " sec on " + date1)

# If an error occurs running geoprocessing tool(s) capture error and write message
except Exception, e:
    # Store information about the error
    tb = sys.exc_info()[2]
    # Write the line number the error occured to the log file
    report.write("Failed at Line %i \n" % tb.tb_lineno)
    # Write the error message to the log file
    report.write("Error: {}".format(e.message))

# close log file
report.close()