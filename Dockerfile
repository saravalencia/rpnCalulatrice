FROM python:3.10.12

# Set the working directory
WORKDIR /app

# Copy the directory contents
COPY . /app

# Install packages specified
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available
EXPOSE 8000

# Database URL
ENV DATABASE_URL=sqlite:///./sql_app.db

# Run main.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]