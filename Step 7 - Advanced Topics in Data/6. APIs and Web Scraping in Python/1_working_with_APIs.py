# # 3.Types of Requests
# import requests
# response = requests.get("http://api.open-notify.org/iss-now.json")
# status_code = response.status_code
# print(status_code)

# # 4.Understanding Status Codes
# import requests
# response = requests.get("http://api.open-notify.org/iss-pass")
# status_code = response.status_code
# print(status_code)


# # 5.Hitting the Right Endpoint
# import requests
# response = requests.get("http://api.open-notify.org/iss-pass.json")
# status_code = response.status_code
# print(status_code)

# # 6.Adding Query Parameters
# import requests
# # Set up the parameters we want to pass to the API.
# # This is the latitude and longitude of New York City.
# parameters = {"lat": 37.78, "lon": -122.41}

# # Make a get request with the parameters.
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# # Print the content of the response (the data the server returned)
# print(response.content)

# # This gets the same data as the command above
# response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# print(response.content)

# # 7.JSON Format
# # Make a list of fast food chains.
# best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
# print(type(best_food_chains))

# # Import the JSON library.
# import json

# # Use json.dumps to convert best_food_chains to a string.
# best_food_chains_string = json.dumps(best_food_chains)
# print(type(best_food_chains_string))

# # Convert best_food_chains_string back to a list.
# print(type(json.loads(best_food_chains_string)))

# # Make a dictionary
# fast_food_franchise = {
#     "Subway": 24722,
#     "McDonalds": 14098,
#     "Starbucks": 10821,
#     "Pizza Hut": 7600
# }

# # We can also dump a dictionary to a string and load it.
# fast_food_franchise_string = json.dumps(fast_food_franchise)
# print(type(fast_food_franchise_string))

# fast_food_franchise_2 = json.loads(fast_food_franchise_string)


# # 8.Getting JSON From a Request
# # Make the same request we did two screens ago.
# import requests
# import json
# parameters = {"lat": 37.78, "lon": -122.41}
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# # Get the response data as a Python object.  Verify that it's a dictionary.
# json_data = response.json()
# print(type(json_data))
# print(json_data)

# first_pass_duration = first_pass_duration = json_data["response"][0]["duration"]
# print(first_pass_duration)



# # 9.Content Type
# import requests
# import json
# parameters = {"lat": 37.78, "lon": -122.41}
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# # Headers is a dictionary
# print(response.headers)
# content_type = response.headers["content-type"]
# print(content_type)

# 10.Finding the Number of People in Space

import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
json_data = response.json()
print(json_data)
in_space_count = json_data["number"]
print(in_space_count)