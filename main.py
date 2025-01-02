from PIL import Image
import os

def resize_imh (img,new_width):
   width,height =img.size
   ratio =height/width
   new_height = int(ratio*width)
   resized_image =img.resize((new_width,new_height))  
   return resized_image 

def main():
   folder =os.listdir()
