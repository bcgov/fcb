# Testing the Container

## Build an image using Docker
```
IMAGE_NAME=franco:v1.3
docker build -t $IMAGE_NAME .
```

## Test / Verify Image

`docker run -d -p 8888:8888 $IMAGE_NAME`

## More info

* [good article on multistage image builds](https://medium.com/trendyol-tech/how-we-reduce-node-docker-image-size-in-3-steps-ff2762b51d5a)
* [quickstart using caddy](https://caddyserver.com/docs/quick-starts/static-files)

# Helm deployments

Service account is required for the github actions to work.  The
first time the helm chart is deployed set the flag
*deploy_service_account* to true, this will create the service
account / roles / role bindings necessary for the service account
that will be used to communicate with OCP4 from github.  Subsequent 
deployments, without this flag being set will igonore the service 
account and related objects.

### First time deploy:



```
SECRETS=<path to the secrets>
helm install smk-fap-fcb helm-charts -f $SECRETS --set deploy_service_account=true
```

# Roles / Service accounts / role binding

## Get a list of the different permissions

`oc describe clusterrole.rbac`

That output describes the possible roles that can be applied.  

