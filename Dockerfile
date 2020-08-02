# We're using Ubuntu 20.10
FROM gengkapak/groovygorilla:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/alanndz/DCLXVI /home/dclxvi/
RUN mkdir /home/dclxvi/bin/
WORKDIR /home/dclxvi/

# Install Requirements, some package havent in Docker
RUN sudo pip3 install -r requirements.txt

CMD ["python3","-m","userbot"]
