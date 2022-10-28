import os
import shutil


hole_path = "C:/Users/lenovo/Desktop/goal/goalLabelXML/"
arm_path = "C:/Users/lenovo/Desktop/goal/soccerLabelXML/"
out_path = "C:/Users/lenovo/Desktop/goal/mergedLabelXML/"

shutil.copy(hole_path+'1.xml', out_path)