from PIL import Image
import os

def resize_img (img,new_width):
   
   width,height =img.size
   ratio =height/width
   new_height = int(ratio*width)
   resized_image =img.resize((new_width,new_height))  
   return resized_image 

def main():
   
   img = Image.open("angry_cat-photo.jpg")
   
   mod_photo = resize_img(img,200) #resizes the photo 
     
   output_folder =os.listdir("Modified-photos") # turns the directory into a list
   output_folder_path = "Modified-photos"
   #place the image into the directory
   output_path = os.path.join(output_folder_path, "angry_cat_resized.jpg")
   #saves the image into the directory
   mod_photo.save(output_path)
   output_folder.append(mod_photo)    
   print(output_folder)             
   for photo in output_folder:
       photo.show()
       
       
if __name__ == "__main__":
    main()
    