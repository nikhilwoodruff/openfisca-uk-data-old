format:
	black . -l 79
test: format
	black . -l 79 --check
	pytest tests