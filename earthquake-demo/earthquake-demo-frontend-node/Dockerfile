FROM node:8.16.0-jessie-slim

ADD . /app
WORKDIR /app
RUN npm install

EXPOSE 8080
CMD ["node", "app.js"]