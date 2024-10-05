import argparse
import sys
import re
from typing import List

def read_html_file(file_path: str) -> str:
    """
    Reads the content of an HTML file from the specified file path.

    Args:
        file_path (str): Path to the HTML file.

    Returns:
        str: The content of the HTML file.
    """
    with open(file_path, 'r') as file:
        return file.read()


# Tests if a "bug" (e.g., <SELECT> tag) is present
def bug_is_present(html_content: str) -> bool:
    """
    Simulates a method call to check if a bug is present in the given HTML content
    by looking for the <SELECT> tag using a regex pattern.

    Args:
        html_content (str): The HTML content to test.

    Returns:
        bool: True if the <SELECT> tag with attributes is present, False otherwise.
    """
    pattern = r'.*<SELECT .*?>.*'
    return bool(re.search(pattern, html_content, re.IGNORECASE))

def split_into_parts(content: str, n: int) -> List[str]:
    """
    Splits the content into n parts as evenly as possible.

    Args:
        content (str): The content to split.
        n (int): The number of parts to split the content into.

    Returns:
        List[str]: A list of n parts of the original content.
    """
    parts = []
    part_size = len(content) // n
    remainder = len(content) % n
    start = 0

    for i in range(n):
        end = start + part_size + (1 if i < remainder else 0)  # Distribute the remainder evenly
        parts.append(content[start:end])
        start = end

    return parts

def delta_debugging(html_content: str) -> str:
    """
    Implements delta debugging to minimize the HTML content that still contains the bug.

    Args:
        html_content (str): The full HTML content to debug.

    Returns:
        str: The minimal HTML content that still contains the bug.
    """
    n = 2  # Start with n = 2 and 𝝙 (CF) as test
    while True:
        parts = split_into_parts(html_content, n)
        
        # Test each 𝝙i and each ∇i
        for i in range(len(parts)):
            # Test 𝝙i
            if bug_is_present(parts[i]):
                # Case 3a: Some 𝝙i causes failure: Goto 1 with 𝝙 = 𝝙i and n = 2
                html_content = parts[i]  # Narrow down the input
                n = 2  # Reset granularity
                break
            # Test ∇i
            complement = ""
            for j in range(len(parts)):
                if j != i:
                    complement += parts[j]
            if bug_is_present(complement):
                # Case 3b: Some ∇i causes failure: Goto 1 with 𝝙 = ∇i and n = n - 1
                html_content = complement  # Narrow down to the complement
                n = n - 1  # Reduce granularity
                break
        else:
            # Case 3c: No test causes failure:
            if 2 * n <= len(html_content):
                # If granularity can be redefined (n*2 <= |𝝙|), go to step 1 with 𝝙 = 𝝙 and n = n * 2
                n = n * 2
            else:
                # Otherwise: Done, return the 1-minimum test
                return html_content

def main(file_path: str) -> None:
    """
    The main function that reads the HTML file, applies delta debugging, 
    and prints the minimal content containing the bug.

    Args:
        file_path (str): The path to the HTML file.
    """
    html_content = read_html_file(file_path)

    minimal_select_content = delta_debugging(html_content)

    print("Minimal content containing the bug:")
    print(minimal_select_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process an HTML file for delta debugging.')
    parser.add_argument('file_path', type=str, help='Path to the HTML file')

    args = parser.parse_args()
    
    if args.file_path is None:
        print("Error: Missing required argument 'file_path'", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    main(args.file_path)

