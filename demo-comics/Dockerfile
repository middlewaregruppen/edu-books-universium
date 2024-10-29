FROM python:3.9
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY templates /app
CMD ["uvicorn", "demo-comics:app","--host","0.0.0.0","--port","8000", "--log-level", "debug"]