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

## Output Parameters

* Docker version tag        ${{ steps.calculateImageTag.outputs.DOCKER_VERSION_TAG }}
  example: (docker.pkg.github.com/frantarkenton/smk-fap-fcb/smk-fap-fcb:20210123-0244)
* timestamp                 ${{ steps.calculateImageTag.outputs.TIMESTAMPTAG }}
* repo name                 ${{ steps.calculateImageTag.outputs.REPO }} 
  (example: smk-fap-fcb )

## Summary of functionality

* Calculates an image tag
* Download the openshift client
* Caches the Issue url in the configmap $REPO-gh-issues-cm (only dev namespace)
* Builds the docker image using the dockerfile
* Caches the image tag in the configmap $REPO-imagetag-cm
* tags the issue associated with the PR with the timestamp tag




