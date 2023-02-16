from python:3.11-buster
RUN apt-get update -y
RUN apt-get install tk -y
#CMD ["/app/main.py"]
#ENTRYPOINT ["python3"]
