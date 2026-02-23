import json
from pathlib import Path

def save_to_file(result, date, month, year, directory="bankersadda-current-affairs"):
    file_path = Path(directory) / str(year) / str(month) / f"{date}-{month}-{year}.json"
    if  not file_path.exists():

        print(f"Saving data to file for {date} {month} {year}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        print(f"File saved successfully: {file_path}")
    
    else:
        print(f"File already exists: {file_path}")
    return    