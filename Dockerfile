FROM python:3.9.18-slim
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 8501
VOLUME [ "/app" ]
CMD ["streamlit", "run", "streamlit_app.py"]
