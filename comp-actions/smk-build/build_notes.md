# Overview

Calculates an image tag based on a timestamp, caches it in a config map in
openshift.  creates a docker image, uploads to github packages.

# Build Details

## Input parameters
* OPENSHIFT_SERVER_URL  url to the openshift instance
* OPENSHIFT_TOKEN_DEV   api key for a service account associated with that 
                        instances dev namespace
* GHCR_USER             github user who has a personal access token configured
                        for access to the repos packages
* GHCR_TOKEN            the personal access token for the user above
* DOCKER_REGISTRY       the path to the docker registry (docker.pkg.github.com)



