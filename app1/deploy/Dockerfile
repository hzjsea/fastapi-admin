# 实例 dockerfile
FROM python:3.6.8
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT env
WORKDIR /code/
# Install dependenciec
ADD ./docker/api /code/
ADD ./app/ /code/app/
ADD ./common/ /code/common
ADD ./script/ /code/script
ADD ./secret/ /code/secret
ADD ./main.py /code/main.py
RUN pip install -r requirements.txt \
    && pip install --upgrade pip

ADD ./docker/api/config /root/.cargo/
RUN ./init.sh

EXPOSE 8000
CMD ["python", "main.py"]