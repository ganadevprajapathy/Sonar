import os
from PIL import Image

def resize_images(input_folder, output_folder, resize_size):
  """
  Resizes images in a folder and saves them in a different folder.

  Args:
      input_folder: Path to the folder containing the images to resize.
      output_folder: Path to the folder where the resized images will be saved.
      resize_size: A tuple (width, height) specifying the desired output size.
  """

  # Create the output folder if it doesn't exist
  os.makedirs(output_folder, exist_ok=True)

  for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
      # Get the full path of the image
      image_path = os.path.join(input_folder, filename)

      # Open the image
      img = Image.open(image_path)

      # Resize the image
      resized_img = img.resize(resize_size, resample=Image.Resampling.LANCZOS)

      # Get the filename without extension
      basename, _ = os.path.splitext(filename)

      # Create the output filename with the original name and resized suffix
      output_filename = f"{basename}_resized.{img.format}"

      # Save the resized image in the output folder
      output_path = os.path.join(output_folder, output_filename)
      resized_img.save(output_path)

# Example usage
input_folder = '/home/republic/Documents/Ganadev/Sonar/Datasets/Data Preparation 4/mine_like_object_right'
output_folder = '/home/republic/Documents/Ganadev/Sonar/Datasets/Data Preparation 5/mine_like_object_right'
resize_size = (400, 64)  # You can change the desired size here

resize_images(input_folder, output_folder, resize_size)
