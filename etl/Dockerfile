FROM python:3.11-alpine

RUN apk --no-cache update sudo bash
RUN addgroup -S news_scrapper && adduser news_scrapper -S -G news_scrapper news_scrapper

RUN echo "news_scrapper:admin" | chpasswd

RUN echo "news_scrapper ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER news_scrapper

WORKDIR /home/etl/news

COPY --chown=news_scrapper:news_scrapper . .

COPY --chown=news_scrapper:news_scrapper requirements.txt .

RUN pip install -r requirements.txt

CMD ['tail','-f','/dev/null']
