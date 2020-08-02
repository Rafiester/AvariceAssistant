# Cz we are Arch User
FROM gengkapak/archlinux:latest
USER gengkapak

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/alanndz/DCLXVI /home/gengkapak/dclxvi/
RUN mkdir /home/gengkapak/dclxvi/bin/
WORKDIR /home/gengkapak/dclxvi/

# Install Requirements, some package havent in Docker
RUN sudo pip3 install -r requirements.txt

CMD ["python3","-m","userbot"]
