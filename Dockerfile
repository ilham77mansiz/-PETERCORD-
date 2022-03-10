#Ilham Mansiez
#Petercord Userbot
#Tentang AKU DAN DIA
FROM  ilhammansiz17/ilham-mansiez-petercord:Petercord-Userbot

RUN git clone -b Petercord-Userbot https://github.com/ilham77mansiz/-PETERCORD- /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ilham77mansiz/-PETERCORD-/Petercord-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
