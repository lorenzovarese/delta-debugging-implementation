# delta-debugging-implementation

Student: Lorenzo Varese

This project contains an implementation of the Delta Debugging algorithm in Python. The algorithm aims to minimize the input that triggers a specific bug in an HTML file (e.g., the presence of a `<SELECT>` tag).

## Prerequisites

- Python 3.x
- The `argparse` module is used for command-line argument parsing (included in standard Python libraries).

## Usage

To use the delta debugging implementation, follow the instructions below:

1. Clone the repository or download the `delta_debugging.py` script.
2. Ensure you have a file containing your HTML content (e.g., `htmlPage.txt`).

### Running the Script

To run the delta debugging script, use the following command:

```bash
python delta_debugging.py htmlPage.txt
