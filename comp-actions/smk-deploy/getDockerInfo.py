''' Simple script that will retreive the following parameters
from an openshift instance
'''

class getDockerInfo:

    def __init__(self):
        self.slurpArgs()

    def slurpArgs(self):
        parser = argparse.ArgumentParser(description='Provide parameter used to construct the gwa config file.')
        parser.add_argument("--OCService", help="openshift service that the route should bind to")
        parser.add_argument("--reponame", help="unique name for your smk app, usually the name of your repository.")
        parser.add_argument("--OCNamespace", help="The openshift namespace that the app resides in.")
        parser.add_argument("--servicePort", help="The port that the open shift service is configured for.")
        parser.add_argument("--kongDomain", help="The domain suffix that will be created.")


class test:

    def __init__(self):
        self.populateArgs()

    def populateArgs(self):
        repoName = 'franTarkenton/smk-fap-fcp-comp'
        registry = 'docker.pkg.github.com'
