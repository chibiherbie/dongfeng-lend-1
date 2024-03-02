FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .

CMD ["npm", "run", "serve"]
