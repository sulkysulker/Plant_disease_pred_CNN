# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create Streamlit config folder
RUN mkdir -p /root/.streamlit

# Copy config.toml into Streamlit config folder
COPY config.toml /root/.streamlit/config.toml

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit app (bind to all network interfaces)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
