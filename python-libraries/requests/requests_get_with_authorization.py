import requests      
import configparser   

# Read the GitHub access token from a configuration file
config = configparser.ConfigParser()

# specify the path to the configuration file
config.read('E:\\python-master\\code\\config.ini')   

# read the GitHub access token from the 'DEFAULT' section
github_token = config['DEFAULT']['github_token']  

# Set the API endpoint and authentication headers
api_endpoint = 'https://api.github.com/user/repos'   

# set the authorization header using the GitHub access token
headers = {'Authorization': f'token {github_token}'}   

# Set the parameters for the API request
parameters = {'type': 'private', 'per_page': 5, 'sort': 'updated'}  

# Make a GET request to the API endpoint to get a list of all the private repositories
#  associated with the user
response = requests.get(api_endpoint, headers=headers, params=parameters)  

# Print the name of each private repository
for repo in response.json():   
    print(repo['name']) 