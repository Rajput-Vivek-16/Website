from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vivek@269'  
app.config['MYSQL_DB'] = 'vivek'  

mysql = MySQL(app)

@app.route('/', methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        # Initialize variables
        a_2_data = None
        year_data = None

        # Handle search and filter options
        if 'selector' in request.form:
            cursor = mysql.connection.cursor()
            selector = request.form.get('selector')
            search_term = request.form.get('box')

            # Check the type of search and execute the appropriate query
            if selector == 'bond_number':
                cursor.execute("SELECT * FROM purchaser WHERE bond_number = %s", (search_term,))
            elif selector == 'filter':
                filter_type = request.form.get('filter_type')
                cursor.execute(f"SELECT * FROM purchaser WHERE {filter_type} = %s", (search_term,))
            a_2_data = cursor.fetchall()
            cursor.close()
        
        # Handle company/individual selection
        elif 'company_individual' in request.form:
            cursor = mysql.connection.cursor()
            company_individual = request.form.get('company_individual')

            # Query data related to the selected company/individual
            cursor.execute("SELECT * FROM purchaser WHERE Name_of_Purchaser = %s", (company_individual,))
            a_2_data = cursor.fetchall()

            # Query year data with the required change for Denominations column
            cursor.execute("""
                SELECT COALESCE(YEAR(Date_of_Purchase), 'Unknown') AS Year, COUNT(*) AS Num_Bonds,
                       SUM(CAST(REPLACE(Denominations, ',', '') AS UNSIGNED)) AS Total_Value
                FROM purchaser
                WHERE Name_of_Purchaser = %s
                GROUP BY COALESCE(YEAR(Date_of_Purchase), 'Unknown')
            """, (company_individual,))
            year_data = cursor.fetchall()
            cursor.close()
        
        # Handle political party selection (new question part)
        elif 'political_party' in request.form:
            cursor = mysql.connection.cursor()
            political_party = request.form.get('political_party')

            # Query data related to the selected political party
            cursor.execute("SELECT * FROM politics WHERE Name_of_Political_Party = %s", (political_party,))
            a_2_data = cursor.fetchall()

            # Query year data with the required change for Denominations column
            cursor.execute("""
                SELECT COALESCE(YEAR(Date_of_Purchase), 'Unknown') AS Year, COUNT(*) AS Num_Bonds,
                       SUM(CAST(REPLACE(Denominations, ',', '') AS UNSIGNED)) AS Total_Value
                FROM politics
                WHERE Name_of_Political_Party = %s
                GROUP BY COALESCE(YEAR(Date_of_Purchase), 'Unknown')
            """, (political_party,))
            year_data = cursor.fetchall()
            cursor.close()

        # Query distinct names of companies and political parties
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT DISTINCT Name_of_Purchaser FROM purchaser")
        companies = cursor.fetchall()

        cursor.execute("SELECT DISTINCT Name_of_Political_Party FROM politics")
        political_parties = cursor.fetchall()
        cursor.close()

        # Render the template with the results and other required data
        return render_template("index.html", companies=companies, political_parties=political_parties, a_2_data=a_2_data, year_data=year_data)
    
    # Handle GET requests
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT DISTINCT Name_of_Purchaser FROM purchaser")
        companies = cursor.fetchall()
        
        cursor.execute("SELECT DISTINCT Name_of_Political_Party FROM politics")
        political_parties = cursor.fetchall()
        cursor.close()

        # Render the template with the initial data (companies and political parties)
        return render_template("index.html", companies=companies, political_parties=political_parties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=True)
