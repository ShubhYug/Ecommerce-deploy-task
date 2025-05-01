# Use a Node base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Expose the port React runs on
EXPOSE 3000

# Start the React app in development mode
CMD ["npm", "start"]
