# templates/default_template.py

# Import necessary libraries
import os

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directories for the project
SRC_DIR = os.path.join(BASE_DIR, 'src')
TEST_DIR = os.path.join(BASE_DIR, 'tests')
DOC_DIR = os.path.join(BASE_DIR, 'docs')

# Create the directories
os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)
os.makedirs(DOC_DIR, exist_ok=True)

# Define the main Python file
MAIN_PY = os.path.join(SRC_DIR, 'main.py')

# Create the main Python file
with open(MAIN_PY, 'w') as f:
    f.write("# main.py\n\n")
    f.write("# Import necessary libraries\n")
    f.write("import os\n\n")
    f.write("# Define the main function\n")
    f.write("def main():\n")
    f.write("    print('Hello, World!')\n\n")
    f.write("# Run the main function\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    main()\n")

# Define the test Python file
TEST_PY = os.path.join(TEST_DIR, 'test_main.py')

# Create the test Python file
with open(TEST_PY, 'w') as f:
    f.write("# test_main.py\n\n")
    f.write("# Import necessary libraries\n")
    f.write("import unittest\n")
    f.write("from src import main\n\n")
    f.write("# Define the test case\n")
    f.write("class TestMain(unittest.TestCase):\n")
    f.write("    def test_main(self):\n")
    f.write("        self.assertEqual(main.main(), 'Hello, World!')\n\n")
    f.write("# Run the tests\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    unittest.main()\n")

# Define the documentation file
DOC_MD = os.path.join(DOC_DIR, 'README.md')

# Create the documentation file
with open(DOC_MD, 'w') as f:
    f.write("# README.md\n\n")
    f.write("This is the documentation for the project.\n")
