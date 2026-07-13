FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && cd datasets && python train.py
EXPOSE 8501
CMD ["cd", "datasets", "&&", "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

[client]
showErrorDetails = false

[logger]
level = "error"

[server]
headless = true
runOnSave = false
