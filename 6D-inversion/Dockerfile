FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./apeer_main.py .
COPY ./invert_6D.py .
COPY ./module_specification.json .

ENTRYPOINT [ "python", "./apeer_main.py" ]
