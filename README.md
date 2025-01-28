# package-doctor 👨‍⚕️

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Suffering from `package.json` dependency chaos? 😩  `package-doctor` 👨‍⚕️ to the rescue!  This Python script automatically scans your `package.json` and updates `date-fns` and `next` versions to your desired specifications, ensuring dependency sanity and project consistency.

## 📖 Table of Contents

- [✨ Features](#-features)
- [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Script](#running-the-script)
- [⚙️ Configuration](#️-configuration)
- [🛠️ Usage](#️-usage)
- [Output Explanation](#output-explanation)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🧑‍💻 Author](#-author)

## ✨ Features

- **Automated Dependency Correction:**  Specifically targets and corrects versions for `date-fns` and `next` dependencies in your `package.json`.
- **Customizable Desired Versions:** Easily modify the script to adjust the target versions for `date-fns`, `next`, or add more dependencies to manage.
- **Descriptive Console Output:** Provides clear and informative messages with emojis to indicate changes made, successes, or issues encountered during the process.
- **Checks Both `dependencies` and `devDependencies`:** Ensures comprehensive coverage by scanning both sections of your `package.json` for the specified dependencies.
- **Error Handling:** Gracefully handles common issues like missing `package.json` file or invalid JSON format, providing helpful error messages.
- **Non-destructive (mostly):**  Only modifies the `package.json` file if changes are needed and outputs to the console if no updates are required. (Always recommended to backup your `package.json` before running any script that modifies it).

## 🚀 Getting Started

Get started with `package-doctor` in just a few simple steps!

### Prerequisites

- **Python 3.x:** You need Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Download the Script:** Download the `update_dependencies.py` script (or copy the code from this repository) and save it to your local machine.
2.  **Place in your Project:**  Ideally, place the script in the root directory of your project where your `package.json` file is located. This makes running the script easier.

### Running the Script

1.  **Open your Terminal:** Navigate to the directory where you saved the `update_dependencies.py` script and your `package.json` file using your terminal or command prompt.
2.  **Execute the Script:** Run the script using the Python interpreter:

    ```bash
    python update_dependencies.py
    ```

    If your `package.json` is in a different location, you can specify the path as an argument:

    ```bash
    python update_dependencies.py path/to/your/package.json
    ```

3.  **Observe the Output:** The script will analyze your `package.json` and output descriptive messages to your console, indicating any changes made or if no updates were needed.

## ⚙️ Configuration

The script is configured through the `desired_dependencies` dictionary within the `update_dependencies.py` file.

```python
desired_dependencies = {
    "date-fns": "^3.0.0",
    "next": "14.2.23"
}
