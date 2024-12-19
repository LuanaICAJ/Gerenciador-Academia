FROM python:3.10

COPY requirements.txt requirements.txt 
COPY entrypoint.sh entrypoint.sh 
RUN chmod +x entrypoint.sh

COPY . .

RUN python3 -m venv .venv && . .venv/bin/activate \
&& pip install -r requirements.txt

ENTRYPOINT ["bash", "./entrypoint.sh"]
