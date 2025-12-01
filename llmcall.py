import ollama # atm ollama is the only tool that supports deepseek-ocr
import re
import os
import  json
from codetiming import Timer
from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic import ValidationError
from validation_structure import ResumeStructure
from json_structures import json_structure, example_json


def process_file(file_path: str, filename: str, output_folder: str, ocr_model: str, logic_model: str):
    with Timer(name="file_total", text="  > Total time for " + filename + ": {:.2f}s"):

        # --- STEP 1: OCR ---
        print("  > Reading image...")
        try:
            ocr_response = ollama.chat(
                model=ocr_model,
                messages=[{'role': 'user', 'content': 'Free OCR.', 'images': [file_path]}]
            )
            raw_text = ocr_response['message']['content']
        except Exception as e:
            print(f"  > OCR Failed: {e}")
            return
        
        # --- STEP 2: JSON Formatting ---
        print("  > Extracting and Validating JSON...")
        valid_data = get_valid_json_from_model(raw_text, logic_model)
        
        if valid_data:
            save_json(valid_data, filename, output_folder)
        else:
            print("  > JSON Validation Failed for {filename}.")

def get_valid_json_from_model(raw_text: str, logic_model: str, max_retries: int = 3):
    prompt = f"""            
            
            You are a data extraction assistant. Below is raw text from a resume.
            Extract the data and format it EXACTLY as this JSON structure:
            {json_structure}
            
            Rules:
            1. Output MUST be valid JSON.
            2. Use "school name" (with a space) as the key for education.
            3. For 'skills.skill_name', provide a single string containing the list of skills.
            
            RAW TEXT:
            {raw_text} 
                
            Example of valid JSON:
            {example_json}
                
            If any field is missing in the raw text, use empty strings or empty arrays as appropriate.
            """
    
    #Calling with pydantic-ai provides automatic validation from the validation structure given
    #Call the model with retries
    try:
        model = OpenRouterModel(
            model_name=logic_model,
        )
        
        agent = Agent(
            model,
            output_type=ResumeStructure,
            system_prompt=prompt
        )
        
        result_content = agent.run_sync()
        
        json_content = result_content.output
        
        json_string = json_content.model_dump_json()
        
        cleaned_json = clean_json(json_string)
        return cleaned_json
    except ValidationError as ve:
        print(f"  > Validation Error: {ve}")

    except Exception as e:
        print(f"  > Logic Model Error: {e}")
            
    return None
            
# --- JSON CLEAN ---
def clean_json(text: str) -> str:
    # Clean Markdown Code Blocks (if model adds ```json ... ```)
    match = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

# --- JSON SAVE ---
def save_json(json_content: str, filename: str, output_folder: str):
                # Changes resume.jpg -> resume.json
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{base_name}.json"
                output_path = os.path.join(output_folder, output_filename)

                # Write to file
                try:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(json_content)
                    print(f"  > Saved JSON to: {output_path}")
                except Exception as file_error:
                    print(f"  > Error saving file: {file_error}")