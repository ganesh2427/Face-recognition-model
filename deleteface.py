import requests

url = "https://api.edenai.run/v2/image/face_recognition/delete_face"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "providers": "amazon",
    "face_id": "88a448b9-a41d-408a-87f7-b6903058b1f7"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQ1NDgyODAtNjNmZC00MmEzLWI2M2QtNDI5YTI4ZDliNTc2IiwidHlwZSI6ImFwaV90b2tlbiJ9.W2qckEzb4fsWyJfyL3mRHZjQeg-l81hMI87t2-82yvk"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

# def deleteface(face_id):
#     url = "https://api.edenai.run/v2/image/face_recognition/delete_face"

#     payload = {
#         "response_as_dict": True,
#         "attributes_as_list": False,
#         "show_original_response": False,
#         "providers": "amazon",
#         "face_id": "911aa445-302c-4524-afdf-663291cb7ee6"
#     }
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQ1NDgyODAtNjNmZC00MmEzLWI2M2QtNDI5YTI4ZDliNTc2IiwidHlwZSI6ImFwaV90b2tlbiJ9.W2qckEzb4fsWyJfyL3mRHZjQeg-l81hMI87t2-82yvk"
#     }

#     response = requests.post(url, json=payload, headers=headers)