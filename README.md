# Scenario
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

Then rotate image. After rotation again identifies boxes to get new coordinates of ages. After that segmentation is began. In segmentation all the boxes cropped and create segment images.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/2.jpg)

We use google vision API to identify numbers and letters. It is pretty much accurate API. Then those words and characters are returned by API. After that we use logical function to identify if it is student Id, student name or sign. This function create an array which saves as 2 dimensions for rows and column. This arrays passes to the database and it stores information about that student. 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/44.jpg)

Then visualize the data from barcharts.

#Line Detection
The technique is mainly based on horizontal and vertical black runs proc-essing as well as on image / text areas estimation in order to remove line segments that belong to these areas. Initially, a series of morphological operations with appropriate structuring elements is performed in order to link potential line breaks and to enhance line segments.
	The following are the distinct steps of the suggested line detection technique:
(I)  horizontal and vertical line estimation
(ii) enhancement of line estimation using the removal of image / text areas.

## Horizontal and vertical line estimation

After refinement of this result, this calculation of lines will be done by eliminating line segments belonging to image / text areas. The proposed line detection algorithm is based on the processing of horizontal and vertical black runs and a collection of morphological operations with appropriate structuring elements to connect potential line breaks and improve line segments.
The average character height AH that was measured in Section 2.1 depends on all the parameters used in this step. Starting with the IM binary image (1s corresponding to text regions and 0s corresponding to context regions).
We take the following steps: 
STEP 1 : We proceed to a series of image IM morphological operations with appropriate structuring elements. Our target is to connect line breaks or dotted lines, but not to connect neighboring characters. We measure IMH and IMV images for horizontal and vertical line detection.
STEP 2 : Both 1s of IMH and IMV images that belong to high-length and small-width line segments are translated to L mark values. In the case of horizontal lines, all IMH 1s belonging to horizontal black length ranges larger than AH and vertical black length ranges smaller than AH are translated to L.In the case of vertical lines, all IMV 1s belonging to vertical black lengths greater than AH and to horizontal black lengths less than AH are converted to L lengths.
STEP 3 : IMH and IMV images are smoothed accordingly in horizontal and vertical directions in order to set all short runs that have a value other than L to L. Horizontal runs of IMH pixels with values not equal to L and lengths less than AH are set to L in the case of horizontal lines.Vertical runs of IMV pixels with values not equal to L and a length less than AH are set to L in the case of vertical lines.
STEP 4 : Horizontal and vertical lines in IMH and IMV images, respectively, are de-defined from all linked components with a length greater than 2 AH of L-valued pixels.

## Enhancement of line estimation using the removal of image / text areas.

The measurement of image / text areas is achieved by performing horizontal and vertical image IMn smoothing for pixels that do not belong to the horizontal or vertical lines detected. All related components of great height (> 3AH) belong to graphics, images or text after this smoothing.In this point, as vertical and horizontal lines are omitted, tables will not appear as individual connected components in the final smooth picture.

We take the following steps: 
1. By setting all horizontal runs with 0's that have a duration of less than 1.2AH to L, we lead to a horizontal smoothing of image IMV. 
2. By setting all vertical runs with 0's that have a duration of less than 1.2AH to L, we lead to vertical smoothing.
3. IT image / text areas are specified in the resulting IMV image from L-valued linked components with a rectangle height greater than 3 AH.

Read the file from the correct direction as the first step, using the threshold to convert the input image to a binary image and invert it to get a black background and white lines and fonts.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/3.jpg)

## Screen Shot :

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/4.jpg)

The next step is to describe the kernel for the detection of rectangular boxes, and the tabular structure afterwards. First, we determine the length of the kernel and then the vertical and horizontal kernels, so that all vertical lines and all horizontal lines are detected later.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/5.jpg)

The next step is the detection of the vertical lines. 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/6.jpg)

## Screen Shot : 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/7.jpg)

And now the same for all horizontal lines.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/8.jpg)

## Screen Shot : 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/9.jpg)

As a next step, by weighting both with 0.5, we combine the horizontal and vertical lines into a third picture. To detect each cell, the goal is to get a simple tabular structure.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/10.jpg)

## Screen Shot :

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/11.jpg)

# Rotate image
First identifies cross points to detect edges of the boxes. After Identifying of boxes processing take one box and get 2 edges to detect angle. Because we need to know the existing angles and the angles we want to get. The table should be rotate as usual

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/12.jpg)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/13.jpg)

Then rotate image according to angle 
 
Reade image 
img = cv2.imread(file) 
Rotate image using imutils function 
img = imutils.rotate(img, angle=360 - angle) 
Write rotated image as rotated.png 
cv2.imwrite(dir+"rotated.png",img) 

## Rotated Image :

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/14.jpg)

After rotation again identifies boxes to get new coordinates of ages. cells.  that's why we use vhimg.

vhimg = cv2.imread(vhPath)
vhimg = imutils.rotate(vhimg, angle=360 - angle)
cv2.imwrite(dir+"img_vh.jpg", vhimg)

img_vh.jpg

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/11.jpg)

# Boxes
Boxes(img_vh_) : method is mainly created to separate and identify the each cell on the given table image and return two arrays.
Input    : cropped main table image(this will contain only vertical and horizontal line)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/15.jpg)

Output : two arrays will be return
1.      Binarized image array with replace 1 with 255. 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/16.jpg)

2.      Coordinates of the identified corners of the boxes with their mean values of x coordinates and Y coordinates ( which can be use as coordinates of the  centroid of identified boxes) 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/17.jpg)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/18.jpg)

here we are converting incoming image into gray scale (img2). And save the image in format of array for manipulate later.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/19.jpg)

in this line we are dilate and inverting the values of the pixels (like 1 to 254, like 255 to 0)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/20.jpg)

Here we binarized our array to do that we use sum of mean and standard deviation value as a threshold value. After this line our array will only have 0’s and 1’s.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/21.jpg)

Label and find the number of boxes.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/22.jpg)

From this for loop we added the x, y coordinates and centroid coordinates of the boxes to an array called box[].

# Identify word and signature
This part mainly focusing on identify words, segmenting, and set identified student number, title, student name, signature to 2 dimension array. 
At the beginning this process need to get box which means 4 coordinates and centroid of each boxes.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/23.jpg)

then loop through each boxes and assign edges and centroids to variables. So we can easily crop this segment using edges.
There a multiple sizes of segments comes with boxes, we only need cells of the tables, so we have to select specific sizes of segment. According to samples of signing sheets we select segment which difference between x3 and x1 less than 1000. So we can get what are the necessary segments. After that we saved it for further processing.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/24.jpg)

Next step is to read those segments. First we used tesseract as optical character recognition tool but letter testing we found out lot of issues regarding with identifying character with that tool. So we had to move to Google OCR. It more intelligent than Tesseract. Lot of issues were solved from it. 

Then we read each boxes by calling Google Vision API.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/25.jpg)

Next step we identify title. We skip titles which is not necessary to include in the array because it is already exist in the Database as column title. But in this step we need to do really necessary thing, it is to get x1 and x3 of Signature title. Student signatures aren’t cropped current way by boxes algorithm due to unnecessary cross points. We need this width to crop student signatures. Height get from the student name segment’s y1 and y3, from this 2 points, crop of signature can be done.

Before -

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/26.jpg)

After - 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/27.jpg)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/28.jpg)

Next step is go through the identified word and detect is it a student No, title or student name. Assign matrix column for that word or number. We got 0th column as signature, 1st column as student name, 2nd column as title and 3th column as student number.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/29.jpg)

Signature recognition step we use colour range to identify blue colour, cv2.inRange will create a mask (binary array) from that pixels, then use that mask to count number of white pixel. That count >1500 we detected as it was signed. 

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/30.jpg)

Mask :

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/31.jpg)

Not assign items to 0th row matrix

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/32.jpg)

then set items to columns of matrix, somehow situations like Metrix -column is filled then next item also owns that Metrix -column then we detect that word need to have new Metrix-row. After that all new items goes to that row. In this step also set identified signature to  matrix-column with student name.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/33.jpg)

then select resize array to remove 0th matrix-row and send to database

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/34.jpg)

Output : [(873, '10000409', 'Ms', 'MS Dilshanika Perera', 'true'), (874, '10009301', 'Mr', 'CWM A Shehan Abeyrathne', 'false'), (875, '10009302', 'Mr', 'BAKM Chithrananda', 'true'), (876, '10009303', 'Ms', 'W Shashini Minosha De Silva', 'false'), (877, '10009304', 'Mr', 'KLUdara Maduranga Liyanage', 'true'), (878, '10009306', 'Mr', 'Hansa Anuradha Wickramanayake', 'true')]

# Store attendance in database
The need to visualize real-time (or near real-time) data has been and still is the most important daily driver of many businesses. Microsoft SQL Server has a lot of capabilities to visualize streaming data and in this case, I will address this issue using Python. Also a python Dash package for building web applications and views. Dash is built on Flask, React and Plotly and offers a wide range of capabilities to build interactive web applications, visual and visual connectors.
SQLite is an information-related program. Without 'Lite' in the name it may contain more information than Terabyte 'Lite' part is really related to the fact that the system is' empty bones'. Provides ways to create and query information with a simple command line interface but not much more. In SQL Study we used the Firefox plugin to provide the GUI (Graphical User Interface) in the SQLite data engine.
It is very simple and often very easy to think of SQL tables. All data manipulation, cutting, price editing, abuse and merging associated with SQL and SQL tables can all be accomplished. The SQL table can always be on the disc and once you have access to it, it is the SQLite data engine that does the job. This allows you to work with tables that are too large for your Python environment that may not have full capture memory at all.
A common use case for SQLite databases is to capture large data sets, using SQL commands from Python to cut and dice and perhaps integrate data within a database system to reduce the size of the Python object that can process it properly and restore results to the Data Center.

## Receive data stored on SQLite using Python
We will demonstrate the use of the sqlite3 module by connecting to the SQLite database using both Python and using pandas.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/35.jpg)

## Connects to SQLite database
The first thing we need to do is to import the sqlite3 library, we will import pandas at the same time for convenience.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/36.jpg)

The next thing we need to do is create a connector cursor and give you a variable. We do this using the link point indicator method.
The interface allows us to transfer SQL statements to the database, processed and returned results. To create a SQL statement using the execute () of the cursor object. The only parameter we need to pass to execute () is a string that contains the SQL query we wish to perform.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/37.jpg)

The execute() method does not actually return any data, it simply indicates that we want the data provided using the SELECT statement.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/38.jpg)

The scope of the built-in function () produces whole numbers between the first given number in the stop number. Using a loop, we can measure the sequence of numbers generated by a range () function.
In for i in range (), i iterator variable. To understand what i for range () means in Python, we first need to understand the range () function. The range () function uses a generator to generate numbers within a range, it does not create all the numbers at once. Produces the next value only if required for loop iteration. For each loop iteration, Python generates the next value and assigns the iterator variable i.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/39.jpg)

The SQL INSERT INTO statement is used to add new records to the table. While adding a record to a table, it is not mandatory to provide the total number of columns, we can only add a few columns using the INSERT INTO statement and the number of remaining columns to be set to work for that record.
And then insert a row of data and Save (commit) the changes.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/40.jpg)

Instead of fetching all rows (which may not be feasible), we can fetch row by row. We also fetch the column names.
Before we can apply the query results we need to use the fetchall () method for the cursor. The fetchall () method returns the list. Each item in the Tuple list contains values from a single row of tables. You can upgrade items in Tuple in the same way you would in a list.

# Create Table
A SQLite table can be created on an in-memory database or on a disk file based database. Creating a table in SQLite involves first selecting a database file and loading it. And in SQLite, tables can be created in the in-memory databases as well. Here this is the table that we created for our project. The table has 5 columns as Id in inreger, StudentsNo in varchar, Title in varchar, StudentName and Signature in varchar. And Id is the primary key of this table.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/41.jpg)

## Database content

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/42.jpg)

# Visualization 
After identifying the  student Id, student name or sign. It creates an array which saves as 2 dimensions for rows and columns. This array passes to the database and it stores information about the student. Using the following code we will create a graph to represent the attendance details that are identified. 

In here, we retrieve student’s data from the database and plot the graph in order to represent attendance details. It will display the total number of days that the relevant student attended the lectures according to their student id number.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/43.jpg)

Following graph is displayed when executing the above code. The graph represents the attendance details of students.

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/Sheet2.PNG)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/Sheet3.PNG)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/Sheet4.PNG)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/Sheet5.PNG)

![](https://github.com/pasindumadushan/TableDataExtractor/blob/master/Readme%20Inages/Summery of 2,3,4,5 Sheets.PNG)


