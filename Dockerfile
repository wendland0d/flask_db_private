FROM tiangolo/uwsgi-nginx:python3.11

RUN sudo apt-get update -y && apt-get upgrade -y

COPY .. /app
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["start.sh"]