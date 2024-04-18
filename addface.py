import requests

url = "https://api.edenai.run/v2/image/face_recognition/add_face"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "providers": "amazon",
    "file_url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Indian_Prime_Minister_Narendra_Modi.jpg"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQ1NDgyODAtNjNmZC00MmEzLWI2M2QtNDI5YTI4ZDliNTc2IiwidHlwZSI6ImFwaV90b2tlbiJ9.W2qckEzb4fsWyJfyL3mRHZjQeg-l81hMI87t2-82yvk"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)


# import requests

# def addface(file_url):
#     url = "https://api.edenai.run/v2/image/face_recognition/add_face"

#     payload = {
#         "response_as_dict": True,
#         "attributes_as_list": False,
#         "show_original_response": False,
#         "providers": "amazon",
#         "file_url": file_url
#     }
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQ1NDgyODAtNjNmZC00MmEzLWI2M2QtNDI5YTI4ZDliNTc2IiwidHlwZSI6ImFwaV90b2tlbiJ9.W2qckEzb4fsWyJfyL3mRHZjQeg-l81hMI87t2-82yvk"
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     json_response = response.json()

#     face_ids = json_response.get('amazon', {}).get('face_ids', [])
#     return ', '.join(face_ids)

# if __name__ == "__main__":
#     response_face_ids = addface("https://upload.wikimedia.org/wikipedia/commons/9/99/Samantha_at_10_Enradhukulla_Teaser_Launch.jpg")
#     print(response_face_ids)




