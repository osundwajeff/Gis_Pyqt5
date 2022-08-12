tatu# pyqt5

## Geoprocessing tool

In this assignment you are going to implement your own **GUI-based Python** program with
**PyQt5**. You have to design it yourself from scratch and put it together in **QT Designer**. There
is a list of required GUI elements that will allow the user to provide the needed input for the
program. The program will use arcpy but it is intended to be a standalone program, so it's not
supposed to be run as a script tool inside **ArcGIS**, and that's why it needs its own GUI. The
program will realize a simple workflow for extracting features from a shapefile on disk based
on **selection by attribute** and **selection by location**.

#### Your program will provide the GUI that allows the user:
- **to select the two input files (country file and POI file)**
- **to provide the name of the target country**
- **to specifiy the name of the output shapefile that will be produced with the extracted shop features**
- **to indicate whether all shops or only shops of a particular type should be extracted (and if so, which type)**

All files making up your project should be included in your submission for this assignment
including the .ui file created with QT Designer. Please also include a screenshot showing the
GUI of your program while the program is being executed.

### Requirements
```
#Python=3.7
#Arcpy module=3.7
#ArcGIS Pro
```
### App interface
![](https://github.com/osundwajeff/pyqt5/blob/main/main_program/GisProgram.png)
