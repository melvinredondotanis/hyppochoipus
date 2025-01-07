# Hyppochoipus

This project celebrates the start of each academic year with a mini-sorting ceremony inspired by the iconic houses of the magical Harry Potter universe.

## The Houses

| House           | Description                                                                                                                                                              | Motto                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Segfaultdor** | The house of the bold, unafraid to crash their programs. These developers thrive on the thrill of fatal errors and face memory dumps with courage.                       | *"If it crashes, we restart!"*                           |
| **Algodaigle**  | Purists of optimization and complex algorithms. Algodaigle members reject inefficient loops and redundant code, striving for the most elegant and optimized solutions.   | *"O(log n) or nothing!"*                                 |
| **Stackouffle** | Heroes of developer forums, experts at solving problems through their legendary mastery of Stack Overflow. They always find a solution, even under pressure.             | *"Oh, it's not so bad!"*                                 |
| **Pythontard**  | Wizards of rapid and flexible development. They prefer high-level languages and avoid static typing. Their code is fluid, efficient, and often written in a single line. | *"Why make it complicated when you can keep it simple?"* |

## How It Works

During the ceremony, each new student takes part in a series of interactive questions. These questions delve into their skills, interests, and values in development. At the end of the dialogue, the magical sorting hat, **Hyppochoipus**, announces their house, highlighting their unique talents and potential.

Here’s a glimpse of possible dialogues:

- **Curiosity and solving complex problems**: *"I sense in you an insatiable thirst for knowledge and limitless creativity. Algodaigle is the perfect house to fuel your curiosity and let you explore your passions."*
- **Ambition and leadership**: *"Your ambition and determination are remarkable. Pythontard will be the ideal place to help you achieve your dreams and aim ever higher."*
- **Teamwork and loyalty**: *"Your loyalty and cooperative spirit are invaluable qualities. Stackouffle will allow you to shine while fostering a strong collective mindset."*
- **Courage and a taste for adventure**: *"Your courage and thirst for adventure make you a perfect fit for Segfaultdor, where you can face all challenges with bravery."*

## Installation

### Prerequisites

- \>= Python 3.9 or Python 3.10 <=
- Git
- Virtualenv (optional but recommended)
- Ollama

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/melvinredondotanis/hyppochoipus.git
    cd hyppochoipus
    ```

2. **Optional:** Create and activate a virtual environment:

    Linux/macOS:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

    Windows:
    ```powershell
    python -m venv env
    .\env\Scripts\Activate.ps1
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create the model with ollama:
    ```bash
    ollama create hyppochoipus -f models/[en or fr]/Modelfile
    ```

5. Run the application:
    ```bash
    python main.py
    ```

## Configuration

To configure the application, you can edit the following files:

`students.json`:
```json
{
    "students": [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve"
    ]
}
```

## Authors

- **Melvin Redondo Tanis** - *Initial work* - [melvinredondotanis](https://github.com/melvinredondotanis)
- **Rémi Marçais** - *Contributor* - [rmarcais](https://github.com/rmarcais)
