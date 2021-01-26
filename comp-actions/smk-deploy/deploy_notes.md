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

### Description

Provide all the required inputs described below, or, said differently, include
all the required parameters and not the one optional parameter (OPENSHIFT_TOKEN_PRD)
provide all the required inputs

### Input parameters:

* OPENSHIFT_SERVER_URL  url to the openshift instance
* OPENSHIFT_TOKEN_DEV:  token used to authenticate to the dev oc project namespace.
* GHCR_USER: the username of a github user that has been configured with a personal 
                access token that can read github packages.  For some weird reason you 
                need to authenticate to be able to pull a container that is hosted on 
                github.
* GHCR_TOKEN: The token that goes with the GHCR_USER.
* DEBUG_DEPLOY: No longer used, was there to allow for debugging.
* OPENSHIFT_TOKEN_PROD: (optional) If deploying to prod then supply this parameter.

### Step parameters populated:

* Repository Name:         ${{ steps.getRepo.outputs.REPONAME}}
* GHCR_USER email address: ${{ steps.getGithubEmail.outputs.EMAIL }}
* Docker Registry          ${{ steps.getDockerRegistry.outputs.IMAGE_REGISTRY}}
* Docker Image Tag         ${{ steps.getDockerImageTag.outputs.DOCKER_VERSION_TAG}}
* Github Issue Url         ${{ steps.getIssueUrl.outputs.ISSUE_URL}}
* Deploy Environment Tag   ${{ steps.getOcNamespaceAndLogin.outputs.ENVTAG}}
* Vanity Url               ${{ steps.kongconf.outputs.VANITY_URL }}


Dev deploys will perform the following steps:

* Login to Openshift - dev.  Even if doing a prod deploy, need to connect to
    dev to get the image tags that were cached during the build 
* Extract the github repo name from the 'github.repository' parameter
    and make available `${{ steps.getRepo.outputs.REPONAME }}`
* Get the email address associated with the input `GHCR_USER`
* Calculate the Github container registry path (example... `docker.pkg.github.com/bcgov/smk-fap-fcb/smk-fap-fcb`)
* Extract the image tag from the configmap `$REPONAME-imagetag-cm` (example: `20210122-0059` )
* Extract the issue url that was populated into the dev namespace config map.  (this should be changed, see this
  step for notes)
* Log into prod oc namespace if its a prod deploy otherwise stay in dev.
* Run the helm chart
* Update the GH issue, with links to the oc route.
* Download the GWA command line tool (disabled for prod)
* Configure the kong route using the gwa command line tool (disabled for prod)
* Add kong vanity url to the ticket (disabled for prod)

