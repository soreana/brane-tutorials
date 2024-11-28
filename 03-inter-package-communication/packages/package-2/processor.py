#!/usr/bin/env python3
import json
import os

def process_message(input_json):
    # Parse the input JSON string
    data = json.loads(input_json.replace("'", '"'))
    
    # Extract and process the fields
    message = data.get("message", "No message provided").upper()
    timestamp = data.get("timestamp", "Unknown time")
    source = data.get("source", "Unknown source")
    
    # Construct a processed response
    result = {
        "original_message": message,
        "processed_at": "Package 2",
        "received_from": source,
        "timestamp": timestamp
    }
    return result

if __name__ == "__main__":
    # Read the JSON input from stdin (simulated input for testing)
    input_json = json.loads(os.environ['INPUT_JSON'])
    
    # Process the input and produce the result
    output = process_message(input_json)
    
    # Print the result as a JSON string
    print(f'result_json: "{output}"' )

