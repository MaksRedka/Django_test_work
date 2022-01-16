FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /Django_test_work
WORKDIR /Django_test_work
COPY requirements.txt /Django_test_work/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./mysite /Django_test_work/