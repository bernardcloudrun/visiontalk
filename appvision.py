from flask import Flask, request, jsonify
from google.cloud import vision
import io
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Get the image from the request
        image_file = request.files['image']
        
        # Initialize Google Cloud Vision client
        client = vision.ImageAnnotatorClient()

        # Read the image file
        content = image_file.read()
        image = vision.Image(content=content)

        # Perform image labeling
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # Format the response
        result = {label.description: label.score for label in labels}

        return jsonify(result)
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
