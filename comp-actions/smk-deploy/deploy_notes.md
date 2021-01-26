# Overview of the deploy action

What it does?  A bunch of stuff, but ultimately deploys an smk application.
If the prod token (OPENSHIFT_TOKEN_PRD) is provided it does a prod deploy, 
otherwise its a dev deploy.  The OPENSHIFT_TOKEN_PRD is configured as an 
optional input.

This action works in conjunction with the other composite action that exists
in this repo (`comp-actions/smk-build`).

The build caches the following information in the dev namespace. The deployments
to prod and to dev need to recover this information allowing them to deploy the 
image that was previously built in the dev step.

# Details

## Dev Deployments

Provide all the required inputs described below, or, said differently, include
all the required parameters and not the one optional parameter (OPENSHIFT_TOKEN_PRD)
provide all the required inputs

Dev deploys will perform the following steps:

* Login to Openshift - dev.  Even if doing a prod deploy, need to connect to
    dev to get the image tags that were cached during the build 
* Extract the github repo name from the 'github.repository' parameter
    and make available `${{ steps.getRepo.outputs.REPONAME }}`
* Get the email address associated with the input `GHCR_USER`
* Calculate the Github container registry path (example... `docker.pkg.github.com/bcgov/smk-fap-fcb/smk-fap-fcb`)
* Extract from the configmap `$REPONAME-imagetag-cm` the image tag (example: `20210122-0059` )
* Get the oc project name that is currently pointed to from 'namespaces-cm' and verify that
    its dev (if no OPENSHIFT_TOKEN_PRD var was provided... otherwise prod)
    and verify that it aligns with the namespace that is expected

    Dev Parameters:
        - Repository Name:         ${{ steps.getRepo.outputs.REPONAME}}
        - GHCR_USER email address: ${{ steps.getGithubEmail.outputs.EMAIL }}
        - Docker Registry          ${{ steps.getDockerRegistry.outputs.IMAGE_REGISTRY}}
        - Docker Image Tag         ${{ steps.getDockerImageTag.outputs.DOCKER_VERSION_TAG}}
