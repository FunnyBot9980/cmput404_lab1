import requests

print(requests.__version__)
response = requests.get("https://google.com")
print(response)

response = requests.get("https://raw.githubusercontent.com/FunnyBot9980/cmput404_labs/main/lab1.py")

open("file.txt", "w").write(response.content)
