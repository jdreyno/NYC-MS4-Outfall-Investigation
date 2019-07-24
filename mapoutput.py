# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:22:22 2019

@author: JasonReynolds
"""

import os
>>> import arcpy
>>> import_path = r"D:/PROJECTS/Dewberry/Outfall_Data/MS4Outfall_v2.mxd"   # Path of .mxd
... export_path = r"D:/PROJECTS/Dewberry/Outfall_Data/jpg2/F"   # Path of output file
... field_name = "UNITID" # Name of field used to sort DDP
... 
... mxd = arcpy.mapping.MapDocument(import_path) 
... for i in range(1, mxd.dataDrivenPages.pageCount + 1):
...    mxd.dataDrivenPages.currentPageID = i
...    row = mxd.dataDrivenPages.pageRow
...    print row.getValue(field_name)
...    arcpy.mapping.ExportToJPEG(mxd, export_path + "." + row.getValue(field_name) + ".jpg", resolution=300) 
... del mxd