.PHONY: setup lint test clean help

setup:
	@echo "Setting up your environment..."
	bash setup.sh

lint:
	@echo "Running code linting..."
	flake8 src/ || echo "Linting failed. Please fix the issues."

test:
	@echo "Running tests..."
	pytest tests/

clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

help:
	@echo "Available commands:"
	@echo "  make setup     - Run setup script"
	@echo "  make lint      - Run code linter"
	@echo "  make test      - Run test suite"
	@echo "  make clean     - Remove temporary files"
