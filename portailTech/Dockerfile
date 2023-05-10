RUN echo '\
deb http bionic main universe \n\
deb http bionic updates main universe \n\
' > /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y install python3.6 \
    && apt-get install -y install python3-pip \
    && updatedb
    
COPY requirements.txt requirements.txt

COPY pip /etc/

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
EXPOSE 8080

ENV FLASK_APP=app.py

ENTRYPOINT ["python3", "-m", "flask", "run"]
