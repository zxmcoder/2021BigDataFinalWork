FROM centos:centos7
RUN yum install python3 -y
RUN pip3 install flask
ADD ./ /KG_steam
WORKDIR /KG_steam
EXPOSE 8888
CMD ["python3", "app.py"]
