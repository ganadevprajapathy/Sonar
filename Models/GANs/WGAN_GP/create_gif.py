from PIL import Image, ImageDraw, ImageFont
import os


def create_gif(folder_path, output_filename, image_step, font_size=30):
  """
  Creates a GIF animation from images in a folder.

  Args:
      folder_path (str): Path to the folder containing images.
      output_filename (str): Name of the output GIF file.
      image_step (int): Step size between images to include (every 100th or 1000th).
      font_size (int, optional): Size of the font for image number display. Defaults to 30.
  """
  images = []
  font = ImageFont.truetype("DejaVuSans.ttf", font_size)

  for i, filename in enumerate(os.listdir(folder_path)):
    if i % image_step == 0:  # Include image every `image_step`
      image_path = os.path.join(folder_path, filename)
      image = Image.open(image_path)

      # Add image number text
      draw = ImageDraw.Draw(image)
      text_width, text_height = draw.textsize(f"{i+1}", font=font)
      draw.text((10, 10), f"{i+1}", font=font, fill=(255, 255, 255))  # White text

      images.append(image)

  images[0].save(output_filename, save_all=True, append_images=images[1:], duration=100, loop=0)  # Adjust duration as needed

  print(f"GIF created: {output_filename}")


if __name__ == "__main__":
  folder_path = "/home/republic/Documents/Ganadev/Sonar/Outputs/GANs/WGAN/Results8/results/"  # Replace with your folder path
  output_filename = "Output1.gif"
  image_step = 10  # Change to 1000 for every 1000th image

  create_gif(folder_path, output_filename, image_step)
