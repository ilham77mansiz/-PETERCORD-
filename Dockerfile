#Ilham Mansiez
#Petercord Userbot
#Tentang AKU DAN DIA

FROM ilhammansiz17/ilham-mansiez-petercord:Petercord-Userbot

RUN git clone -b Petercord-Userbot https://github.com/ilham77mansiz/-PETERCORD-  /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

WORKDIR /home/userbot/

CMD ["python3","-m","userbot"]
