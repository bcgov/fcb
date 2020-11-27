# Overview

AT a high level the CD/CI pipeline used for SMK apps will perform
the following steps:

1. Pull Request (PR) on Github triggers the Build
1. Successful completion of the build will trigger a *dev* deployment to ocp4
1. completion of the *dev* deployment will update the PR issue with a temporary url of the *dev* app.
1. accept/merge of the PR triggers the *prod* deployment.

# Details

## Build

Build is initiated by a PR to Github's master branch.  The build creates a 
docker image and stores it as a [github package](https://github.com/orgs/bcgov/packages?repo_name=smk-fap-fcb)

Images are labelled using a timestamp.

## Deployment Pre-requisites

All actions should NOT fail even without these parameters being populated, 
however they just won't actually do anything.  Once these parameters are populated, subsequent PR's should successfully trigger a deployment to Github.

OPENSHIFT_TOKEN_DEV=<api key for service account used to deploy to dev>
OPENSHIFT_TOKEN_PROD=<api key for service account used to deploy to prod>
OPENSHIFT_TOKEN_URL=<url to openshift instance>
OCP4-HELM-VALUES=<text to put in here is defined below>

### Define Helm Chart Values

Take this template and fill in the correct values, then when complete
put the text into the github secret: **OCP4-HELM-VALUES**

```
app_name: <name of your app, usually same name as github repo>
app_image_pull_secret_params:
  email: <email associated with github account>
  username: <github user id>
  password: <github personal access token>
  registry: <github package registry, example docker.pkg.github.com/bcgov/smk-fap-fcb/smk-fap-fcb>
  imagetag: <image tag to be deployed, example: 20201123-1946>
```





## Dev Deployment

### De

Before any deployments will actually work you need to populate the f

Dev deployments are triggered by a successful build.  All actions beyond the
build will check that the secret: OCP4-SA-KEY.  If the key is not populated 
the actions will proceed but actually do nothing.

Deployments are all handled by the helm chart located in the directory
'helm-charts'.  Deployments also use the parameter


