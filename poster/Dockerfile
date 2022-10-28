FROM python:3.10-alpine

RUN mkdir -p /home/poster
RUN addgroup -S poster && adduser -S poster -G poster

ENV HOME=/home/poster
ENV POSTER_HOME=/home/poster/web

RUN mkdir $POSTER_HOME
RUN mkdir $POSTER_HOME/static
RUN mkdir $POSTER_HOME/media
WORKDIR $POSTER_HOME

RUN apk update && apk add libpq postgresql-dev gcc python3-dev musl-dev postgresql-contrib

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./entrypoint.sh $POSTER_HOME
RUN sed -i 's/\r$//g' $POSTER_HOME/entrypoint.sh
RUN chmod +x $POSTER_HOME/entrypoint.sh

COPY . $POSTER_HOME

RUN python manage.py collectstatic --noinput

RUN chown -R poster:poster $POSTER_HOME

USER poster

ENTRYPOINT ["/home/poster/web/entrypoint.sh"]
