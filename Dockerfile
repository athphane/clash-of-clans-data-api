FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Add debug to see directory contents
RUN ls -la

# One of the following approaches should work
# Option 1: If app is a directory with __init__.py
CMD ["python", "-m", "app"]

# Option 2: If you have a specific entry file
# CMD ["python", "app.py"]

# Option 3: If app is a package with __main__.py
# CMD ["python", "-m", "app"]