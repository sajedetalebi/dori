FROM node:18-alpine

WORKDIR /app

# Configure npm to use a specific registry and timeout
RUN npm config set registry https://registry.npmjs.org/ && \
    npm config set fetch-timeout 600000 && \
    npm config set fetch-retries 5

COPY package*.json ./
RUN npm install --network-timeout 600000

COPY . .

EXPOSE 3000
CMD ["npm", "start"]
