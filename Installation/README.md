
# Django Installation from Git

This guide will walk you through the steps to install Django directly from the Git repository in a virtual environment.

## Prerequisites

Ensure you have the following tools installed on your machine:
- Python 3.x
- Git
- pip (comes pre-installed with Python 3.x)

## Step-by-Step Instructions

### 1. Create a Virtual Environment

First, create a virtual environment to isolate the Django installation. Run the following command:

```bash
python -m venv myenv
```

Replace `myenv` with any name for your environment.

### 2. Activate the Virtual Environment

Activate the environment depending on your operating system:

- **On Linux/macOS**:
  ```bash
  source myenv/bin/activate
  ```

- **On Windows**:
  ```bash
  myenv\Scripts\activate
  ```

### 3. Clone the Django Repository

Clone the Django repository from GitHub using the following command:

```bash
git clone https://github.com/django/django.git
```

This will download the latest Django codebase into a folder called `django`.

### 4. Install Django

Navigate to the Django directory and install Django in your virtual environment using `pip`:

```bash
cd django
pip install -e .
```

The `-e` flag installs Django in "editable" mode, meaning changes to the source code will immediately reflect without needing to reinstall.

### 5. Verify the Installation

To verify the installation, check the installed Django version by running:

```bash
python -m django --version
```

If the command returns the version number, Django has been successfully installed.

## Deactivating the Virtual Environment

When you're done working in the virtual environment, deactivate it by running:

```bash
deactivate
```

## Troubleshooting

If you encounter any issues during installation, ensure that:
- Python 3.x is properly installed.
- Git is installed and configured on your machine.

## Next Steps

You can now create a new Django project or start contributing to Django development. To create a new project, run:

```bash
django-admin startproject myproject
```

Replace `myproject` with your desired project name.

---
Enjoy working with Django!
