# Overview

This doc describes how the various build/deployment github actions work for smk based
apps deployed to openshift.

To take a current SMK repository and deploy it to openshift the following are the steps:

1. Acquire a new openshift set of namespaces (dlv|test|prod|tools)
1. Run the namespace init helm chart 
1. Configure an SMK based app github repo to be deployed to openshift and trigger a build

# Acquire openshift namespace

This task describes the process of requesting a new openshift namespace from the lab.
The request comes with 4 actual namespaces:

* dev
* test
* prod
* tools

Multiple smk apps will be deployed to the namespace that is acquired in this
step.

# Run init helm chart

A smk_namespace helm chart has been created that will add objects to the
namespace that are re-used by each helm chart.

* Github actions service account
* Github actions service account roles
* Github actions service account role bindings
* namespace configmap
* Gateway secrets

# Configure SMK based app for Deployment

To deploy an app to the openshift namespace the following steps need to be taken

1. populate the oc secrets in github
1. populate the github repository with the following secrets:

    * GHCR_TOKEN : The personal access key that is used to pull the image from github packages to openshift (Github needs credentials to access images)
    * GHCR_USER : The username that is associated with the token
    * OPENSHIFT_SERVER_URL: The url to the openshift instance
    * OPENSHIFT_TOKEN_DEV: The api key for the service account created in openshift.  This is the token that allows github actions to communicate with openshift

1. For now, the .github folder and the helm-charts folders need to be copied into the repository.


