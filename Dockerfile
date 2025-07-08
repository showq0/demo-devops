FROM python:3.13-slim

RUN mkdir /app

# put my project to the image inside app dir  
ADD . /app

# we can defince env varibale here 
# starting point as cd command
WORKDIR /app

# RUN python main.py

EXPOSE 3000
# when build or run image
# no space more secure 
ENTRYPOINT [ "python", "main.py" ]