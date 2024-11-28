# Brane Tutorials Repository

Welcome to the **Brane Tutorials** repository! This repository contains step-by-step tutorials, source codes, and video recordings to help you learn and master Brane—a framework for creating and managing workflows.

## Overview

Each tutorial in this repository is designed to guide you through a specific feature of Brane, starting from basic workflows to more advanced concepts like inter-package communication. Whether you're new to Brane or looking to deepen your knowledge, you'll find valuable resources here.

## Table of Contents

| Tutorial                          | Description                                                                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------|
| [1. Hello World](01-hello-world/README.md)         | Learn how to create and run your first "Hello World" workflow in Brane.                        |
| [2. First Package](02-first-package/README.md)     | Discover how to create your first Brane package with Python and use it in a workflow.         |
| [3. Inter-Package Communication](03-inter-package-communication/README.md) | Explore how to connect multiple Brane packages to pass information seamlessly between them. |

## Getting Started

To get started with the tutorials:
1. Clone this repository to your local machine:
   `git clone https://github.com/soreana/brane-tutorials.git`
2. Navigate to the tutorial you're interested in and follow the instructions in its `README.md`.

## Future Tutorials for Brane

Below is a list of planned future tutorials, covering advanced topics to enhance your Brane skills:

| Tutorial                          | Concept                                                                                     | Skills Covered                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Handling Inputs and Outputs       | Build a package that takes user input, processes it, and returns an output. Example: Factorial calculation. | Adding `input` parameters, modifying Python code for dynamic inputs, testing with various inputs. |
| Data Processing Workflow          | Create a package for data extraction, transformation, and loading (ETL). Example: Scraping and processing data. | Handling dependencies like `requests` or `pandas`, defining multiple tasks, structuring modular code. |
| Package with External Libraries   | Build a package using external Python libraries. Example: Generating plots with Matplotlib or Seaborn. | Specifying library dependencies in `container.yml`, including complex Python scripts, visualizing results. |
| Combining Packages with APIs      | Interact with external APIs in a package. Example: Fetching weather data and displaying forecasts. | Adding API calls, handling keys securely, parsing and using API responses.                       |
| Machine Learning Workflow         | Create a package for ML tasks like training models or making predictions. Example: Housing price predictions. | Including ML libraries like Scikit-learn, working with model files, combining ML with data processing packages. |


## Feedback and Contributions

If you have any feedback or ideas for additional tutorials, please feel free to open an issue or submit a pull request. Contributions are always welcome!

---

Happy learning, and enjoy exploring Brane!
