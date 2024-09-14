# Installation of the Hyppochoipus

Welcome to the Hyppochoipus installation guide. Follow the steps below to set up your environment.

## Prerequisites

**recommended**

- Linux
- Python *3.12.5*
- Pip *24.2*
- CUDA *(if you have a compatible GPU)*

## Installation Steps

1. Clone the repository

```bash
git clone https://github.com/melvinredondotanis/hyppochoipus.git
```

2. Access the project directory

```bash
cd hyppochoipus
```

3. Create a virtual environment

```bash
python3 -m venv env
```

4. Activate the virtual environment

    **UNIX-like**

    ```bash
    source venv/bin/activate
    ```

    **Windows**

    ```powershell
    env\Scripts\activate
    ```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Install Ollama

    **Linux**

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

    **macOS/Windows**

    GUI installer [here](https://ollama.com/download)
    
    **Install the Hyppochoipus custom prompt**

    ```bash
    ollama install llama3.1
    ollama create [hyppochoipus Modelfile path]
    ```

7. Run the application

**UNIX-like**

```bash
python main.py
```

**Windows**

```powershell
python main.py
```
