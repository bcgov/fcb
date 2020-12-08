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

With this chart we are trying to re-use a single chart to deploy multiple SMK based apps that have been generated using the SMK command line tool.  Most of the objects defined in the helm chart will be duplicated to create different SMK based apps in the same 
repository.

## objects created by Helm chart that are re-used for each app

* service account (.Values.github_actions_sa.name)
* roles (named after service account with '-role' suffix)
* role bindings (named after service account with '-rb' suffix)
* github actions image pull secrets



Some objects in the helm template will get deployed once, then re-
used by all subsequent deployments.  Other objects in the helm 
chart are created multiple time on a per app basis.  In other words
each different smk app will have its own version of these objects.



```
SECRETS=<path to the secrets>
helm install smk-fap-fcb helm-charts -f $SECRETS --set deploy_service_account=true
```

# Roles / Service accounts / role binding

## Get a list of the different permissions

`oc describe clusterrole.rbac`

That output describes the possible roles that can be applied.  

