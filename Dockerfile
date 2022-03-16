FROM python:3.8.11-slim-buster
RUN mkdir /webapps
WORKDIR /webapps
RUN pip install -U pip setuptools
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


ADD . /webapps/
CMD [ "python", "./cartao_virtual_status.py" ]