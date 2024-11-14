FROM node:18-alpine

WORKDIR /app

# Configure npm for better network handling
RUN npm config set registry https://registry.npmjs.org/ && \
    npm config set fetch-timeout 600000 && \
    npm config set fetch-retries 5

# Install react-scripts globally first
RUN npm install -g react-scripts@5.0.1

COPY package*.json ./
RUN npm install --network-timeout=600000 && \
    npm install react-scripts@5.0.1 --save

COPY . .

EXPOSE 3000
CMD ["react-scripts", "start"]
