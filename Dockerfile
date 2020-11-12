FROM node:lts-alpine
#RUN mkdir /app

# needed assets needs to be copied as a directory, don't see a way 
# around having these two layers as when add assets to the copy command
# it does not create the directory
ADD  assets /app/assets
COPY ["index.html", "package.json", "package-lock.json", "smk-config.json", \
      "smk-init.js", "/app/"]
WORKDIR /app
RUN npm install
ENV PATH=$PATH:/app/node_modules/http-server/bin
EXPOSE 8080
ENTRYPOINT ["node", "/app/node_modules/http-server/bin/http-server", "-p", "8888", "-s" ]
