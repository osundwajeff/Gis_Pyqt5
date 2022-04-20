# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:55:21 2021

@author: Jeff
"""

import sys
import arcpy
 
from PyQt5.Qt import *
 

import gisGUI

arcpy.env.overwriteOutput = True


#========================================== 
# create app and main window + dialog GUI 
# =========================================  
app = QApplication(sys.argv) 
 
# set up main window 
mainWindow = QMainWindow() 
ui = gisGUI.Ui_MainWindow()
ui.setupUi(mainWindow) 
 
ui.actionExit.setIcon(app.style().standardIcon(QStyle.SP_DialogCancelButton)) 
 

#================================== 
# initialize global variables 
#================================== 
result = []                     # global variable for storing query results as list of dictionaries 
arcValidLayers= {}              # dictionary mapping layer names to layer objects       
 
arcpyAvailable = False          # indicates whether is available for import 
runningAsScriptTool = False     # indicates whether script is run as script tool inside ArcGIS 
#=======================================
# run app 
#======================================= 
def selectShapefile():     
    """open file dialog to select existing shapefile and if accepted, update GUI accordingly"""
    points, _ = QFileDialog.getOpenFileName(mainWindow, "Select shapefile", "", "Shapefile (*.shp)")
    if points:
        ui.shapefileinput.setText(points)

    arcpy.MakeFeatureLayer_management(points, 'supermarket_layer', "shop = 'supermarket'")
    print("Make point feature layer complete")
        
def selectShapefile2():     
    """open file dialog to select existing shapefile and if accepted, update GUI accordingly"""
    countries, _ = QFileDialog.getOpenFileName(mainWindow, "Select shapefile", "", "Shapefile (*.shp)")
    if countries:
        ui.shapefileinput2.setText(countries)

    arcpy.MakeFeatureLayer_management(countries, 'Guatemala_layer', "NAME = 'Guatemala'")
    print("make country feature layer complete")


def outputShapefilepath():
    outPath = QFileDialog.getExistingDirectory(mainWindow, "Select Directory:")
    if outPath:
        ui.shapefileoutput.setText(outPath)
        return outPath

def runGeoProcess():
    arcpy.SelectLayerByLocation_management('supermarket_layer', 'WITHIN', 'Guatemala_layer')
    print("Selection By location complete")
    arcpy.FeatureClassToFeatureClass_conversion('supermarket_layer', outputShapefilepath(), 'supermarket_Guatemala')
    arcpy.FeatureClassToFeatureClass_conversion('Guatemala_layer', outputShapefilepath(), 'Guatemala_Country')
    print("Feature class to feature class conversion complete")
    ui.statusbar.showMessage("Process completed")


ui.inputFeatue1.clicked.connect(selectShapefile)
ui.inputFeature2.clicked.connect(selectShapefile2)
ui.outputFeature.clicked.connect(outputShapefilepath)


ui.runTask.clicked.connect(runGeoProcess)



mainWindow.show() 
sys.exit(app.exec_())
