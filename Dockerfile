FROM python
ADD python/* /code/
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
