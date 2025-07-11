import json
from ocr_reader import extract_text_from_image
from gemini_parser import extract_fields_using_gemini
from vector_store import normalize_item_name

def process_receipt(image_path: str):
    text = extract_text_from_image(image_path)
    raw_json_str = extract_fields_using_gemini(text)
    print("Raw JSON from Gemini:", raw_json_str)

    # Convert string to dict (if Gemini returns valid JSON string)
    try:
        data = json.loads(raw_json_str)
        for item in data.get("items", []):
            item["normalized_name"] = normalize_item_name(item["name"])
        return data
    except Exception as e:
        print("Parsing error:", e)
        return None

if __name__ == "__main__":
    result = process_receipt("sample_receipts/bill1.jpg")
    print(json.dumps(result, indent=2))
