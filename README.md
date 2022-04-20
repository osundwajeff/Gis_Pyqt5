# pyqt5

In this assignment you are going to implement your own GUI-based Python program with
PyQt5. You have to design it yourself from scratch and put it together in QT Designer.'\n' There
is a list of required GUI elements that will allow the user to provide the needed input for the
program. The program will use arcpy but it is intended to be a standalone program, so it's not
supposed to be run as a script tool inside ArcGIS, and that's why it needs its own GUI. The
program will realize a simple workflow for extracting features from a shapefile on disk based
on selection by attribute and selection by location. Please download the attached zip file
assignment_CAT_data.zip with the data you will need for this project. Extract the data to a new
folder and check out the two shapefiles that are contained in the zip file, countries.shp and
OSMpoints.shp, in ArcGIS.

**Your program will provide the GUI that allows the user:**
- i. to select the two input files (country file and POI file),
- ii. to provide the name of the target country,
- iii. to specifiy the name of the output shapefile that will be produced with the extracted shop features,
- iv. and to indicate whether all shops or only shops of a particular type should be extracted (and if so, which type).

All files making up your project should be included in your submission for this assignment
including the .ui file created with QT Designer. Please also include a screenshot showing the
GUI of your program while the program is being executed.
