# Inter-Package Communication Tutorial: Overview

Welcome to the "Inter-Package Communication" tutorial for Brane! This tutorial demonstrates how to connect multiple packages within a Brane workflow to pass information seamlessly between them.

## Overview

In real-world applications, tasks are often modular, requiring different components to work together. This tutorial focuses on demonstrating how to:
- Create two packages that communicate via JSON data.
- Build a workflow to connect these packages.
- Enhance the workflow with additional features for smarter execution.

By the end of this tutorial, you will have a deeper understanding of how to design modular workflows and integrate packages to create reusable and scalable pipelines.

## Structure of the Tutorial

This tutorial is divided into the following steps:
1. **Create Package 1**: Learn how to build a package that generates structured data.
2. **Create Package 2**: Develop a package that consumes and processes the data from Package 1.
3. **Build the Workflow**: Write a Brane workflow to connect the two packages.
4. **Enhance the Workflow** (Optional): Add logging or conditional logic for smarter execution.
5. **Test and Run the Workflow**: Run the workflow and review the results.

## Prerequisites

Before starting this tutorial, make sure you:
- Have Brane installed and configured on your machine.
- Completed the [First Package Tutorial](../02-first-package/README.md) to understand the basics of package creation.

# Step 1 - Create Package 1

In this step, we’ll create the first package, which generates structured data. This package will serve as the starting point in our workflow and produce JSON output that will be passed to the second package.

## Overview

Package 1 generates a simple JSON object containing:
- A message
- A timestamp
- The source of the data

This JSON object will be consumed by Package 2 in the next step.

## Files

- `generator.py`: Python script for generating the JSON data.
- `container.yml`: Configuration file for the package.

## Instructions

### Step 1: Write the Python Script
1. Create a file named `generator.py`.
2. Write the following Python code:

```python
#!/usr/bin/env python3
import json
from datetime import datetime

def generate_message():
    data = {
        "message": "Hello from Package 1!",
        "timestamp": datetime.now().isoformat(),
        "source": "Package 1"
    }
    return data

if __name__ == "__main__":
    output = generate_message()
    print(f'message_json: "{output}"')
```

This script generates a JSON object containing a message, the current timestamp, and the source of the data.

### Step 2: Create the `container.yml` File
1. Create a file named `container.yml`.
2. Add the following content to define the package:

```yaml
name: generator
version: 1.0.0
kind: ecu

dependencies:
- python3

files:
- generator.py

entrypoint:
  kind: task
  exec: generator.py

actions:
  'generate_message':
    command:
    input:
    output:
    - name: message_json
      type: string
```

This configuration file:
- Specifies the name (`generator`) and version (`1.0.0`) of the package.
- Lists the required dependencies.
- Defines the entrypoint and actions for the package.

### Step 3: Build the Package
1. Open your terminal and navigate to the directory containing `generator.py` and `container.yml`.
2. Build the package with the following command:
```
brane package build container.yml
```

### Step 4: Test the Package
1. Run the following command to test the package:

```
brane package test generator
```

2. Now you need to select a task to run. We currently have only one task available, `generate_message`, which you can execute by pressing enter.

```
asa@host03:~/$ brane package test generator
? The function the execute ›
❯ generate_message
```

3. You should see output similar to this:
```
asa@host03:~/$ brane package test generator
✔ The function the execute · generate_message

Result: {'message': 'Hello from Package 1!', 'timestamp': '2024-11-28T02:30:42.702967', 'source': 'Package 1'} [String]
```



---

Happy learning, and enjoy exploring Brane!


---

Happy learning, and enjoy exploring Brane!
