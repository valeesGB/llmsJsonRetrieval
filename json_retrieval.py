import os
from codetiming import Timer
from llmcall import process_file

# Configuration
image_folder = 'resume_image'
output_folder = 'resume_json'
ocr_model = "deepseek-ocr" 
logic_model = "qwen3:14b"

TEST_MODE = True 

def main():
  if not os.path.exists(output_folder):
      os.makedirs(output_folder)

  if not os.path.exists(image_folder):
      os.makedirs(image_folder)

  files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

  if not files:
          print(f"No images found in {image_folder}")
          return

  if TEST_MODE and files:
      files = files[250:350]

  # Global Timer
  with Timer(name="global", text="\n" + "="*40 + "\nTotal Program Runtime: {:.2f} seconds\n" + "="*40):

      for filename in files:
          file_path = os.path.join(image_folder, filename)
          print(f"\nProcessing {filename}...")
          
          process_file(file_path, filename, output_folder, ocr_model, logic_model)
        
       
    
if __name__ == "__main__":
    main()