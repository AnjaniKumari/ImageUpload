from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
@api_view(['POST'])
def imageupload(request):
    if request.method=="POST":
        print("HI")
        input_user=(request.data).dict()
        desc=input_user["text"]
        #print(flow)
        # image=input_user["file"]
        image_name=str(input_user["file"])
        file = request.FILES["file"]
        path = default_storage.save(image_name, ContentFile(file.read())) 
        print(input_user["file"])
        print(path)
        return Response("The attchment uploaded:"+str(image_name)+"    & the description:"+str(desc))

