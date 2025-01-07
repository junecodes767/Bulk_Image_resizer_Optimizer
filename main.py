from PIL import Image
import os

def resize_img (img,new_width=None,new_height=None):
   img = Image.open(img)
   width,height =img.size
   aspect_ratio = width / height
    
   if new_width is not None and new_height is None:
        # If only new_width is provided, calculate new_height
        new_height = int(new_width / aspect_ratio)
   elif new_height is not None and new_width is None:
        # If only new_height is provided, calculate new_width
        new_width = int(new_height * aspect_ratio)
   elif new_width is not None and new_height is not None:
        # If both are provided, adjust them to maintain the aspect ratio
        calculated_new_height = int(new_width / aspect_ratio)
        calculated_new_width = int(new_height * aspect_ratio)
        if calculated_new_height <= new_height:
            new_height = calculated_new_height  # Use height based on width
        else:
            new_width = calculated_new_width  # Use width based on height

    # Resize the image
   
   resized_image = img.resize((new_width, new_height), Image.LANCZOS)
   return resized_image

def main():
    
   #source directory for images
   folder_name =os.listdir("Photos-to-adjust") 
   folder_path =r"C:\Users\noble\Bulk-Image-Resizer-Optimizer\Photos-to-adjust"
   output_folder_path =r"C:\Users\noble\Bulk-Image-Resizer-Optimizer\Modified-photos"
    
 
    
    
   new_folder =os.listdir("Modified-photos")
     # loop through the images
   for photo in folder_name:
      photo_path = os.path.join(folder_path, photo)  # Full path to the image file
      if os.path.exists( photo_path ):
         #resizes the image to desireable size
         modified_image =resize_img(photo_path,400)
         print(f"Photo{photo} resized")
         new_folder.append(photo)
         #add the photo to the new folder
         next_location = os.path.join(output_folder_path ,photo)
         #save the path
         modified_image.save(next_location)
      else: 
         print(f"Photo named {photo} does not exist")
      
if __name__ == '__main__':
   main()