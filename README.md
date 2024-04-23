# Website using Flask 
Welcome to my first Git Repository! I'm Rajput Vivek (23110269), and I've created a project utilizing Flask to build a web application. Here's a step-by-step guide on how to use it:
<br>
<br>
# First convert both PDFs to CSVs by using the Fitz library

db1_political.pdf to politics.csv and db_2 purchaser.pdf to purchaser.csv by using the code which is given in pdf_to_csv.py file.

# Importing CSVs into MySQL 
Before we begin, we need to convert two PDFs into CSV format using the Fitz library. Run the provided code in pdf_to_csv.py to convert:
* db1_political.pdf to politics.csv
* db_2 purchaser.pdf to purchaser.csv
<be>
<br>
We will use MySQL Workbench to create schema named vivek.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/cc32652b-9875-44c6-9970-598cec815282)
<be>
<br>
In this schema, we will import both CSVs in two different tables. Here I am showing how to import CSV in the table of Schema vivek.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/fc9a6e66-000f-4764-b512-df42a917ad06)
<br>
<br>
We have inserted tables namely as purchaser and politics.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/befcc526-e985-4b85-b766-3b1e041501f2)
<br>
<br>
politics table looks like this.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/4f25d118-dd1a-41cd-9895-388d702e6b4b)
<br>
<br>
purchaser table looks like this.
<br> 
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/6071bd0d-2dec-4abb-839f-0c619bbc6c3a)
<br>
<br>
# Switch to VsCode

Now, let's switch to VsCode. Create a new folder containing:
<br>
A folder named templates which includes:
<br>
index.html
<br>
Other necessary files such as main.py.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/2c70004c-d673-420d-be0a-5928757100a6)
<br>
<br>
# Flask 
In main.py, we put the code of main.py 
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/cfae716a-de96-4fe1-92dd-e882ca601672)
<br>
Run this file and click on the link
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/99ded63e-2fe6-4b11-b0dd-a844617ec761)
<br>
We will get a search look at the website.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/be05451b-2694-448c-a602-7942553afc8e)

# Explore the website
e1 We have to enter the bond number, which will give out all purchase and redemption details associated with it.
<br>
![image](https://github.com/Rajput-Vivek-16/Website/assets/167712861/897e9621-0a42-4958-b819-381d23677b84)
<br>
<br>
That's it! We've successfully set up and explored the website. Feel free to reach out if you have any questions or feedback.
<br>
<br>
Happy coding! 🚀







