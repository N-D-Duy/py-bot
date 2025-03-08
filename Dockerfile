FROM ubuntu:latest
LABEL authors="dnd"

ENTRYPOINT ["top", "-b"]