# Hello World Workflow Tutorial

Welcome to the "Hello World" tutorial for Brane! This tutorial introduces the basics of creating and running workflows in Brane by executing a simple "Hello World" script.

## Overview

In this tutorial, you will:
- Learn how to create a Brane workflow.
- Run your first workflow to print "Hello World!" to the console.

This tutorial is designed for beginners who want to get started with Brane and understand its workflow capabilities.

## Files

- `<Youtube Link>`: Video recording of the tutorial.
- `hello_world.bs`: The workflow script used in this tutorial.

## Instructions

### Step 1: Write the Workflow
1. Open a text editor and create a file named `hello_world.bs`.
2. Copy the following workflow into the file:

```
#[on("localhost")]
println("Hello world!");
```

### Step 2: Run the Workflow
1. Open your terminal.
2. Navigate to the directory where `hello_world.bs` is saved.
3. Run the workflow using the following command:

```
brane workflow run hello_world.bs
```

### Step 3: View the Output
If everything is set up correctly, you should see the following output in your terminal:

```
asa@host03$ brane workflow run hello_world.bs
Hello world!
```

## What's Next?

Once you've completed this tutorial, you’re ready to move on to more advanced topics like creating your first package. Check out the [First Package Tutorial](../02-first-package/README.md) for your next steps!

---

Happy learning, and enjoy exploring Brane!

