# using Alpine Edge
FROM mrmiss/userbutt:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b userbutt https://github.com/Rafiester/AvariceAssistant /root/userbutt
RUN mkdir /root/userbutt/bin/
WORKDIR /root/userbutt/

# Make open port TCP
EXPOSE 80 443

CMD ["python3","-m","userbutt"]
