from PIL import Image
import os

def resize_img (img,new_width):
   img = Image.open(img)
   width,height =img.size
   ratio =height/width
   new_height = int(ratio*width)
   resized_image =img.resize((new_width,new_height))  
   return resized_image 

def main():
   folder =os.listdir("Photos-to-adjust")#creates a list of the image files
   folder_path ="Modified-photos"
   # loop through the images
   for photo in folder:
      #resizes the image to desireable size
      modified_image =resize_img(photo)
      #add the photo to the new folder
      next_location = os.path.join(folder_path,photo)
      #save the path
      