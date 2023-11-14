FROM node:18-alpine

RUN apk add dumb-init

COPY ./package.json /app/package.json
WORKDIR /app
RUN npm install

COPY . /app/

EXPOSE 3000

USER node

CMD dumb-init npm run start
