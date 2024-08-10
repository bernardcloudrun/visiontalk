from google.cloud import vision
from google.oauth2 import service_account

# Replace with the path to your JSON key file
credentials = service_account.Credentials.from_service_account_file('C:\\Users\\HP\\Downloads\\mamaegimaonline-638d7aa945e2.json')

# Create a Vision API client
client = vision.ImageAnnotatorClient(credentials=credentials)

# Replace with the path to your image file
with open('C:\\Users\\HP\\Downloads\\WhatsApp Image 2024-08-05 at 05.39.54_e3092367.jpg', 'rb') as image_file:
    content = image_file.read()

# Create an image object
image = vision.Image(content=content)

# Perform label detection on the image file
response = client.label_detection(image=image)

# Print the labels and their confidence scores
labels = response.label_annotations
for label in labels:
    print(label.description, label.score)
