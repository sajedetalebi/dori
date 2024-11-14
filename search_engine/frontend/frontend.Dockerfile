FROM node:18-alpine

WORKDIR /app

# Configure npm for better network handling
RUN npm config set registry https://registry.npmjs.org/ && \
    npm config set fetch-timeout 600000 && \
    npm config set fetch-retries 5

COPY package*.json ./
RUN npm install --network-timeout=600000

COPY . .

EXPOSE 3000
CMD ["npm", "start"]
