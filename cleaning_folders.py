from pathlib import Path

def keep_common_filenames(folder_a, folder_b, dry_run):
    
    c=0
    
    """
    Compares two folders and deletes files that do not have a matching 
    filename (ignoring extension) in the other folder.
    
    Args:
        folder_a (str): Path to the first folder.
        folder_b (str): Path to the second folder.
        dry_run (bool): If True, prints actions without deleting. 
                        If False, deletes the files.
    """
    
    # Convert strings to Path objects
    path_a = Path(folder_a)
    path_b = Path(folder_b)

    # Check if folders exist
    if not path_a.exists() or not path_b.exists():
        print("Error: One or both folder paths do not exist.")
        return

    # Get list of files (ignoring subdirectories)
    files_a = [f for f in path_a.iterdir() if f.is_file()]
    files_b = [f for f in path_b.iterdir() if f.is_file()]

    # Extract just the filenames without extensions (the "stem")
    # sets are used for fast O(1) lookups
    stems_a = {f.stem for f in files_a}
    stems_b = {f.stem for f in files_b}

    # Find the intersection (names that exist in BOTH)
    common_stems = stems_a.intersection(stems_b)

    print(f"--- Processing: {folder_a} ---")
    for file in files_a:
        if file.stem not in common_stems:
            
            if dry_run:
                print(f"[Would Delete] {file.name}")
            else:
                try:
                    file.unlink()
                    print(f"[Deleted] {file.name}")
                except Exception as e:
                    print(f"[Error Deleting] {file.name}: {e}")

    print(f"\n--- Processing: {folder_b} ---")
    for file in files_b:
        if file.stem not in common_stems:
            c=c+1
            if dry_run:
                print(f"[Would Delete] {file.name}")
            else:
                try:
                    file.unlink()
                    print(f"[Deleted] {file.name}")
                except Exception as e:
                    print(f"[Error Deleting] {file.name}: {e}")

    print(f"\nTotal files identified for deletion: {c}")
    
    if dry_run:
        print("\n*** DRY RUN COMPLETE. No files were actually deleted. ***")
        print("*** Call the function with dry_run=False to execute deletion. ***")
        

folder_1 = "C:\\Users\\lisit\\OneDrive\\Desktop\\llmJsonRetrival\\resume_text"
folder_2 = "C:\\Users\\lisit\\OneDrive\\Desktop\\llmJsonRetrival\\resume_json"

keep_common_filenames(folder_1, folder_2, dry_run=False)