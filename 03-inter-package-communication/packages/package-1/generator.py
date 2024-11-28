#!/usr/bin/env python3
import json
from datetime import datetime

def generate_message():
    # Generate a message with structured data
    data = {
        "message": "Hello from Package 1!",
        "timestamp": datetime.now().isoformat(),
        "source": "Package 1"
    }
    return data

if __name__ == "__main__":
    # Convert the dictionary to a JSON string and print it
    output = generate_message()
    print(f'message_json: "{output}"')
