import pytest
import os

# DISCLAIMER: This script is provided "as is" and without warranty of any kind. 
# Use at your own risk. The author shall not be liable for any damages arising from the use of this script.

def run_tests():
    # This function runs a suite of tests using pytest.
    os.chdir('tests')
    pytest.main(['--verbose'])
    os.chdir('..')

def check_coverage():
    # This function checks test coverage using pytest-cov.
    os.chdir('tests')
    pytest.main(['--cov=app', '--cov-report=term-missing', '--verbose'])
    os.chdir('..')

def run_linters():
    # This function runs linters using flake8.
    os.system('flake8 app tests')

def menu():
    # This function displays the menu and allows the user to choose which option to execute.
    while True:
        print('What would you like to do?')
        print('1. Run tests')
        print('2. Check test coverage')
        print('3. Run linters')
        print('4. Exit')
        choice = input('> ')
        if choice == '1':
            run_tests()
        elif choice == '2':
            check_coverage()
        elif choice == '3':
            run_linters()
        elif choice == '4':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    menu()
