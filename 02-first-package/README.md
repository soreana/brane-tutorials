# First Package Tutorial

Welcome to the "First Package" tutorial for Brane! In this tutorial, you will learn how to create and use a Brane package. We’ll walk through building a Python-based package that generates a "Hello World" message.

## Overview

In this tutorial, you will:
- Learn how to create a Brane package using Python.
- Configure the `container.yml` file for the package.
- Build and test your first Brane package.

This tutorial builds on the knowledge from the "Hello World" tutorial and introduces the concept of reusable packages in Brane.

## Files

- `<TBD youtube link>`: Video recording of the tutorial.
- `hello.py`: Python script used to generate the "Hello World" message.
- `container.yml`: Configuration file defining the package.
- `hello-world.bs`: BraneScript workflow to call the package.

## Instructions

### Step 1: Write the Python Script
1. Create a file named `hello.py`.
2. Write the following Python script:

```python
#!/usr/bin/env python3

def hello_world():
    return "Hello, world!"

print(f'output: "{hello_world()}"')

```

- The `hello_world()` function returns the string `"Hello, world!"`.
- The script prints this output to the console in a formatted way.

### Step 2: Create the `container.yml` File

To package this code in Brane, we need a configuration file called `container.yml`. This file defines the package's properties, dependencies, and tasks.

1. Create a file named `container.yml`.
2. Add the following content to define the package:

```YAML
# Generic properties of the package
version: 1.0.0
kind: ecu

# Defines things we need to install
dependencies:
- python3

# Specifies the files we need to put in this package
files:
- hello.py

# Defines which of the files is the file that the framework will call
entrypoint:
  kind: task
  exec: hello.py

# Describe the tasks available in the package, including inputs and outputs.
actions:
  'hello_world':
    command:
    input:
    output:
    - name: output
      type: string
```

### Step 3: Build the Package
1. Open a terminal and navigate to the directory containing `hello.py` and `container.yml`.
2. Build the package with the following command:

```
brane package build container.yml
```

3. You can check the see build image using the following command:

```
asa@host03~/$ docker images
REPOSITORY        TAG               IMAGE ID       CREATED        SIZE
hello_world       1.0.0             207df7e4bb33   10 days ago    213MB
learn             1.0.0             8e0514e4d596   10 days ago    7.1GB
compute           1.0.0             3b32f931ff55   2 weeks ago    5.95GB
visualization     1.0.0             2e7ddbc080ac   2 weeks ago    937MB
brane-reg         3.0.0             9184ec1e1881   5 weeks ago    96.8MB
brane-prx         3.0.0             88594d95c10e   5 weeks ago    91.9MB
brane-drv         3.0.0             0ddad717a042   5 weeks ago    98.5MB
brane-plr         3.0.0             0df4f89f9aa4   5 weeks ago    94.1MB
brane-job         3.0.0             b1831a8dbb41   5 weeks ago    102MB
brane-chk         3.0.0             10a8d42a91e6   5 weeks ago    104MB
brane-api         3.0.0             8d631bd0e382   5 weeks ago    113MB
moby/buildkit     buildx-stable-1   2a89c2764aad   2 months ago   203MB
python            3.8               3ea6eaad4f17   2 months ago   995MB
aux-scylla        3.0.0             3dca5b164211   2 years ago    872MB
scylladb/scylla   4.6.3             3dca5b164211   2 years ago    872MB
```

4. You can also check the list of brane pacakges using the following command:

```
asa@host03~/$ brane package list
 ID          NAME                  VERSION     KIND        CREATED          SIZE
 c63f4a9c    hello_world           1.0.0       ecu         2 weeks ago      92.27 MB
 86518794    visualization         1.0.0       ecu         2 weeks ago      384.38 MB
 42811071    compute               1.0.0       ecu         2 weeks ago      3.90 GB
 a2000e50    learn                 1.0.0       ecu         2 weeks ago      4.58 GB
```

### Step 4: Test the Package
1. Run the following command to test the package:

```
brane package test hello_world
```

2. Now you need to select a task to run. We currently have only one task available, `hello_world`, which you can execute by pressing enter.

```
asa@host03:~/$ brane package test hello_world
? The function the execute ›
❯ hello_world
```

3. You should see output similar to this:

```
asa@host03:~/demo/02-first-package$ brane package test hello_world
✔ The function the execute · hello_world

Result: Hello, world! [String]
```

### Step 5 (Optional): Run the Package in a Workflow
You can use the package you’ve created in a workflow to see how Brane connects workflows and packages. 

1. Create a new file named `hello-world.bs`.
2. Write the following workflow:

```
import hello_world;

#[on("localhost")]
println(hello_world());
```

3. Save the file and run the workflow with the following command:
```
brane workflow run hello-world.bs
```

4. You should see the output:
```
asa@host03:~/$ brane workflow run hello-world.bs
Hello, world!
```

This step demonstrates how packages can be integrated into workflows for modular and reusable pipelines.


## What's Next?

Now that you've created your first Brane package, you're ready to move on to more advanced topics. Check out the [Inter-Package Communication Tutorial](../03-inter-package-communication/README.md) to learn how to connect multiple packages in a workflow. Here are some warm up exercises you can try before going to the next tutorial:

- Modify the Python code to perform more complex tasks.
- Add additional tasks to the `actions` section of `container.yml`.
- Explore other dependencies or combine this package with workflows.

---

Happy learning, and enjoy exploring Brane!
