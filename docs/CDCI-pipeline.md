# Overview

SMK and the SMK command line allow non technical users to easily author
web maps that can consume a variety of different spatial data sets 
including:

* WMS
* ArcGIS Server Rest
* Other misc custom data sources

DataBC wants to be able to publish SMK based apps easily and efficiently into
a single SMK openshift workspace.  The workspace (dev|test|prod|tools) in theory could host 
hundreds of smk apps.  The deployment process should be as automated as possible.

At a high level the CD/CI pipeline used for SMK apps will perform
the following steps:

1. Pull Request (PR) on Github triggers the Build
1. Successful completion of the build will trigger a *dev* deployment to ocp4
1. completion of the *dev* deployment will update the PR issue with a temporary url of the *dev* app.
1. accept/merge of the PR triggers the *prod* deployment.

# Details

The full CD/CI pipeline is handled by github actions.  How the pipeline code
gets added to the repo is still yet to be determined.  Some idea include:

1. code is injected into the repository when the smk-cli tool is run
1. smk repo's inherit from a github templated repo that contains the actions code
1. users copy code into the repo, (likely the inital choice)

The last option is likely how things will initially be handled.  Possibly will
evolve to one of the other options as time allows.

The CD/CI pipeline will be built so that it will simply skip over steps that 
cannot be run due to the absence of secrets.  Once secrets are added to the
repo the next time the action runs it will process what it can based on 
what secrets are populated.

## Build

Build is initiated by a PR to Github's master branch.  The build creates a 
docker image and stores it as a [github package](https://github.com/orgs/bcgov/packages?repo_name=smk-fap-fcb)

Images are labelled using a timestamp.

The build process calculates an image tag, then caches it in OCP as a configmap for 
subsequent deployments.  If the ocp credentials are not populated then the
tag will not get populated.

### Credentials used by Build

* GHCR_TOKEN: used to authenticate to github for different api calls
* GHCR_USER: used to authenticate to github, not actually required for the 
            current flow, but future proofing the code to allow for eventual
            migration from github packages to github container registry 
            (ghcr.io)
* OPENSHIFT_SERVER_URL: the url that is used to communicate with openshift (the url used to authenticate oc cli)
* OPENSHIFT_TOKEN_DEV: service account api key for the oc project.  This key
    is generated the first time the helm chart is run in ocp4.  This is the api key for the dev namespace.  Used by steps that deploy to dev.

## Deployment Pre-requisites

All actions should NOT fail even without these parameters being populated, 
however they just won't actually do anything.  Once these parameters are populated, subsequent PR's should successfully trigger a deployment to Github.

Deployment actions use all the secrets used by the build, and for the action that completes the final deployment to prod the additional secrets are used:

* OPENSHIFT_TOKEN_PROD=<api key for service account used to deploy to prod>
* OPENSHIFT_NAMESPACES=<a configmap with three entries, <dev|test|prod>, where each entry is equal to the ocp namespace used for different envs.

example OPENSHIFT_NAMESPACES secret:
``` json
{
    "dev": "glid27-dev",
    "test": "glid27-test",
    "prod": "glid27-prod"
}
```

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


