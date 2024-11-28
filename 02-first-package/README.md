# Brane Tutorial: Creating a "Hello World" Package with Python

This tutorial demonstrates how to create a Brane package containing Python code that prints a simple "Hello, World!" message.

---

## Step 1: Understanding the Python Code

Here’s the Python script we'll use:

#!/usr/bin/env python3

def hello_world():
    return "Hello, world!"

print(f'output: "{hello_world()}"')

- The `hello_world()` function returns the string `"Hello, world!"`.
- The script prints this output to the console in a formatted way.

---

## Step 2: Preparing the `container.yml` File

To package this code in Brane, we need a configuration file called `container.yml`. This file defines the package's properties, dependencies, and tasks.

Here’s the content of the `container.yml` file:

# Generic properties of the package
name: hello_world
version: 1.0.0
kind: ecu

# Dependencies required to run the package
dependencies:
- python3

# Files to include in the package
files:
- hello.py

# Entrypoint for the package
entrypoint:
  kind: task
  exec: hello.py

# Tasks defined in this package
actions:
  'hello_world':
    command:
    input:
    output:
    - name: output
      type: string

### Key Points:
- `name` and `version`: Specify the package name and version.
- `dependencies`: List required software (e.g., Python 3).
- `files`: Include the Python script, `hello.py`.
- `entrypoint`: Define the main file executed by Brane.
- `actions`: Describe the tasks available in the package, including inputs and outputs.

---

## Step 3: Building the Package

Follow these steps to build the package:

1. Save the Python script as `hello.py`.
2. Place `hello.py` and `container.yml` in the same directory.
3. Open a terminal and navigate to this directory.
4. Run the following command to build the package:

brane package create .

This command packages everything in the current directory into a Brane package.

---

## Step 4: Testing the Package

Once the package is built, test it to ensure it works. Use the following command:

brane task hello_world

If everything is set up correctly, you should see:

output: "Hello, world!"

---

## Next Steps

- Modify the Python code to perform more complex tasks.
- Add additional tasks to the `actions` section of `container.yml`.
- Explore other dependencies or combine this package with workflows.

This tutorial is based on the example from the Brane tutorials page, which you can find [here](https://wiki.enablingpersonalizedinterventions.nl/tutorials/tutorials/2023-04-20/p1_hello_world.html).

---

## Conclusion

Congratulations! You’ve successfully created and tested your first Brane package with Python code. Continue exploring Brane to unlock its full potential!







# First Package Tutorial

Welcome to the "First Package" tutorial for Brane! In this tutorial, you will learn how to create and use a Brane package. We’ll walk through building a Python-based package that generates a "Hello World" message.

## Overview

In this tutorial, you will:
- Learn how to create a Brane package using Python.
- Configure the `container.yml` file for the package.
- Build and test your first Brane package.

This tutorial builds on the knowledge from the "Hello World" tutorial and introduces the concept of reusable packages in Brane.

## Files

- `tutorial-2.mp4`: Video recording of the tutorial.
- `package1.py`: Python script used to generate the "Hello World" message.
- `container.yml`: Configuration file defining the package.

## Instructions

### Step 1: Write the Python Script
1. Create a file named `package1.py`.
2. Write the following Python script:

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
    print(json.dumps(output))

### Step 2: Create the `container.yml` File
1. Create a file named `container.yml`.
2. Add the following content to define the package:

name: package1
version: 1.0.0
kind: ecu
dependencies:
- python3
files:
- package1.py
entrypoint:
  kind: task
  exec: package1.py
actions:
  'generate_message':
    command:
    input:
    output:
    - name: message_json
      type: string

### Step 3: Build the Package
1. Open a terminal and navigate to the directory containing `package1.py` and `container.yml`.
2. Build the package with the following command:
brane package create .

### Step 4: Test the Package
1. Run the following command to test the package:
brane task generate_message
2. You should see output similar to this:
{
  "message": "Hello from Package 1!",
  "timestamp": "2024-11-17T10:23:45.123456",
  "source": "Package 1"
}

## What's Next?

Now that you've created your first Brane package, you're ready to move on to more advanced topics. Check out the [Inter-Package Communication Tutorial](../03-inter-package-communication/README.md) to learn how to connect multiple packages in a workflow.

---

Happy learning, and enjoy exploring Brane!

