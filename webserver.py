# pyServer using Request Lib 
import requests 
import json

# intialize a web server using BASEHttpServer, and convert to Requests lib
# Create on-listening GET Request HTTP port for S3 to extract data 
# Get S3 bucket's excel sheet, using AWS CLI 
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
data = json.loads(r.content)
http_code = r.status_code

print (http_code)


# Parse Raw Data to Pandas and put in async while running the following.. 
# Local machine to create a new SQL table to set up sql schema 
# Call for instances from EC2 Store output data in SQLite/MySQL 

# Parse SQL data to Seaborn 
# Send HTTP Request to Web Front End of Seaborn with Flask -> Django for Full Stack Application to manage data set creation
# Set up Nginx Server to serve forever
# Create S3 Bucket to store and manage excel file, using python scripting 
# Write pyTest for every component 
