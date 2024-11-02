# Base Image
FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Update APT repository & Install packages
RUN apt-get update \
    && apt-get install -y python3-dev python3-pip python3-distutils 
    # && apt-get install -y cmake build-essential tmux nano

WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3","telegram_bot.py"]

# CMD ["/bin/bash","-c", "tail -f /dev/null"]
