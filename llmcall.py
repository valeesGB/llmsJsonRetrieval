import ollama
import re
import os
import  json
from codetiming import Timer
from pydantic import ValidationError
from validation_structure import ResumeStructure
from json_structures import json_structure, example_json

def process_file(file_path: str, filename: str, output_folder: str, raw_text_folder: str,ocr_model: str, logic_model: str):
    with Timer(name="file_total", text="  > Total time for " + filename + ": {:.2f}s"):

        # --- STEP 1.1: OCR ---
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
        
        # --- STEP 1.2: TXT ---
        print("  > Saving Raw Text...")
        
        try:
            base_name = os.path.splitext(filename)[0]
            output_filename = f"{base_name}.txt"
            output_path = os.path.join(raw_text_folder, output_filename)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(raw_text)
            print(f"  > Saved Raw Text to: {output_path}")
        except Exception as file_error:
            print(f"  > Error saving file: {file_error}")
        
        # --- STEP 2: JSON Formatting ---
        print("  > Extracting and Validating JSON...")
        valid_data = get_valid_json_from_model(raw_text, logic_model)
        
        if valid_data:
            final_json_str = json.dumps(valid_data.model_dump(by_alias=True), indent=2)
            save_json(final_json_str, filename, output_folder)
        else:
            print("  > JSON Validation Failed for {filename}.")

def get_valid_json_from_model(raw_text: str, logic_model: str, max_retries: int = 3):
    system_prompt = f"""            
            
            You are a data extraction assistant. Below is raw text from a resume.
            Extract the data and format it EXACTLY as this JSON structure:
            {json_structure}
            
            Rules:
            1. Output MUST be valid JSON.
            2. Use "school name" (with a space) as the key for education.
            3. For 'skills.skill_name', provide a single string containing the list of skills.
            
            RAW TEXT:
            {raw_text}
            """

    user_message = f"""       
                
            Example of valid JSON:
            {example_json}
                
            If any field is missing in the raw text, use empty strings or empty arrays as appropriate.
            """

    # History of the conversation
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_message}
    ]            
    
    #Call the model with retries
    for attempt in range(max_retries):
        try:
            response = ollama.chat(
                model=logic_model,
                messages=messages,
                options={'temperature': 0.1} # Low temp = more consistent JSON
            )
            json_content = response['message']['content']
            
            cleaned_json = clean_json(json_content)
            validated_json = ResumeStructure.model_validate_json(cleaned_json)
            return validated_json
        except ValidationError as e:
            print(f"  > Attempt {attempt + 1} Structure invalid: {e}")
            error_msg = f"JSON validation error: {e}\n Correct the JSON structure and output it again."
            # Append interaction to history so model "remembers" its mistake
            messages.append({'role': 'assistant', 'content': json_content})
            messages.append({'role': 'user', 'content': error_msg})
        
        except Exception as e:
            print(f"    > Attempt {attempt+1}: General Error (likely invalid JSON syntax): {e}")
            messages.append({'role': 'assistant', 'content': json_content})
            messages.append({'role': 'user', 'content': "Invalid JSON syntax. Ensure keys are quoted and brackets match."})
            
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
        