
FROM python:3.9

RUN pip install mysql-connector-python

WORKDIR /usr/app/src

COPY programa_monumentos.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./programa_monumentos.py" ]

