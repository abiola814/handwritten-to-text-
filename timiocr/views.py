from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import json
import os
import sys
import requests
import time
from io import BytesIO

missing_env = False
# Add your Computer Vision subscription key and endpoint to your environment variables.



def home(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        endpoint = 'https://handwritten-to-text2.cognitiveservices.azure.com'
        subscription_key = '113fad96017f4f6891354e104c42daad'
        text_recognition_url = endpoint + "/vision/v3.1/read/analyze"

# Set image_url to the URL of an image that you want to recognize.
        image_url = 'https://hardtotext2' + file_url
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        im='/home/abiola/Pictures/Screenshot from 2022-01-04 13-56-52.png'
        imageu=open(im,'rb')
        data = {'url': image_url}
        response = requests.post(
            text_recognition_url, headers=headers, json=data)
        response.raise_for_status()

        # Extracting text requires two API calls: One call to submit the
        # image for processing, the other to retrieve the text found in the image.

        # Holds the URI used to retrieve the recognized text.
        operation_url = response.headers["Operation-Location"]

        # The recognized text isn't immediately available, so poll to wait for completion.
        analysis = {}
        poll = True
        while (poll):
            response_final = requests.get(
                response.headers["Operation-Location"], headers=headers)
            analysis = response_final.json()
            
            print(json.dumps(analysis, indent=4))

            time.sleep(1)
            if ("analyzeResult" in analysis):
                poll = False
            if ("status" in analysis and analysis['status'] == 'failed'):
                poll = False

        polygons = []
        if ("analyzeResult" in analysis):
            # Extract the recognized text, with bounding boxes.
            polygons = [(line["boundingBox"], line["text"])
                        for line in analysis["analyzeResult"]["readResults"][0]["lines"]]

        # Display the image and overlay it with the extracted text.
    
        final=''
        for polygon in polygons:
            vertices = [(polygon[0][i], polygon[0][i+1])
                        for i in range(0, len(polygon[0]), 2)]
            text = polygon[1]
            wordss=str(text)

            final=final+ wordss
            hs=open("hest.txt","a")
            hs.write(text + "\n")

        return render(request, 'base.html', {'file_url':file_url})

    return render(request,"base.html",)
