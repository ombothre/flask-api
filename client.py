import requests

def send(x):

    # Define input data for prediction
    input_data = {'input': x}  # Example input

    # Make a POST request to the API
    response = requests.post('http://127.0.0.1:5000/predict', json=input_data) #add your url

    if response.status_code == 200:
        prediction = response.json()
        y = prediction['prediction'][0]

    else:
        return 404

    return y

#Input
gender = input("Enter gender (Male/Female) : ")
age = int(input("Enter age : "))
sal = int(input("Enter salary : "))

x = [gender,age,sal]

y = send(x)

if y == 1:
    print("User will not buy from you")

elif y == 0:
    print("User will buy from you")

else:
    print("Error")