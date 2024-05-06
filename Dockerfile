FROM odoo:15
USER root
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
