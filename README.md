##Scenario
You are asked to create a student attendance management system based on the signing sheets. The signing sheets have a specific layout which is static. Students can sign the sheet at a given space using different color pens.
•	The admin staff would take snapshots using their smart phones of these signing sheets and provide you the image files.
•	They also provide you a text file containing the student indices and subject related information.
•	Once you receive those files, your program should process the image and text content and identify whether a student is present or absent based on the appearance of a signature.
 
The main focus is with two key technologies:
•	Image processing
•	Data visualization

# Introduction
This project is regarding the day to day problem of university attendance sheet, Which is printed by university with proper format. Lot of universities still use this kind of a signing sheet because it is classic way and it can do easily. Problem is, end of the day those informations need to record in the system. Currently it is inserted in the system by a person. It take too much time to count all the signatures according to the student. Some time signature not match with the student original signature. This kind of a situation need to identify.

In this project there a several major image processing parts.
At the beginning of the execution it detect vertical lines and horizontal lines of the image, then identifies cross points to detect edges of the boxes. After Identifying of boxes processing take one box and get 2 edges to detect angle. 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/1.jpg)
