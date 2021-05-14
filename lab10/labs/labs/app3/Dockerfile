FROM node:alpine

WORKDIR /app #changing work directory to /app

COPY . . 

RUN npm install #install the necessary modules when building the image 

EXPOSE 3000

CMD [ "node", "app3.js" ]
