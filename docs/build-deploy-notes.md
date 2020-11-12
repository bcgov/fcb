# testing the container

## build an image
IMAGE_NAME=franco:v1.3
docker build -t $IMAGE_NAME .

## test the image
docker run -d -p 8888:8888 $IMAGE_NAME

