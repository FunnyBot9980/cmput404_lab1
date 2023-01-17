import requests

print(requests.__version__)
response = requests.get("https://google.com")
print(response)

response = requests.get("https://raw.githubusercontent.com/FunnyBot9980/cmput404_lab1/main/lab1.py")

open("lab1.py", "wb").write(response.content)
