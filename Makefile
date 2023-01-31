tw-install:
	npm install -D tailwindcss
	npx tailwindcss init

tw-watch:
	npx tailwindcss -i ./static/styles/input.css -o ./static/styles/output.css --watch

tw-minify:
	npx tailwindcss -i ./static/styles/input.css -o ./static/styles/output.css --minify

init:
	python -m venv venv
	source venv/bin/activate

install: requirements.txt
	python -m pip install --upgrade pip
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run:
	python app.py

test:
	pytest

clean:
	rm -rf .pytest_cache \
	handlers/__pycache__ \
	models/__pycache__ \
	modules/__pycache__ \
	tests/__pycache__ \
	utils/__pycache__

env: .env.example
	cp .env.example .env