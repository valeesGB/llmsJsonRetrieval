# firstprototype.py just useless file for testing

'''import os
import ollama

TEST_MODE = True 

image_folder = 'resume_image'
model_name = "deepseek-ocr:3b"

json_structure = """
{
  "experience": [{"title": "", "duration": "", "responsibilities": []}],
  "skills": [{"title": "soft skills", "skls": []}, {"title": "technical skills", "skls": []}],
  "education": [{"title": "", "school name": "", "grade": ""}],
  "bio": [{"age": null, "location": "", "job position": ""}],
  "projects": [{"title": "", "description": ""}]
}
"""

PROMPT = f"Extract the text from the image and format it as a valid JSON object matching this structure: {json_structure} and write bububabasssklmn at the end"

files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
files.sort()

if TEST_MODE and files:
    files = files[:1] 

for filename in files:
    print(f"Sending {filename} to Ollama...")
    
    response = ollama.chat(
        model=model_name,
        messages=[{
            'role': 'user',
            'content': 'Free OCR.',
            'images': [os.path.join(image_folder, filename)]
        }]
    )
    print(response['message']['content'])'''