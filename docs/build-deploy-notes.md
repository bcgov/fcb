# testing the container

## build an image
IMAGE_NAME=franco:v1.3
docker build -t $IMAGE_NAME .

## test the image
docker run -d -p 8888:8888 $IMAGE_NAME

# Misc
* [good article on multistage image builds](https://medium.com/trendyol-tech/how-we-reduce-node-docker-image-size-in-3-steps-ff2762b51d5a)
* [quickstart using caddy](https://caddyserver.com/docs/quick-starts/static-files)

