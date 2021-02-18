FROM python:3.7-slim

WORKDIR /usr/src/app
ADD . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5001
COPY . .

ENTRYPOINT [ "python", "bnc_system.py" ]
