import yaml
import argparse
import sys

class GWAConfig:

    def __init__(self):
        #self.outputFile = outFile
        self.service = None
        self.silverUrl = None
        self.endPointDir = '/'
        self.namespace = None
        self.destUrlPrefix = None

    def slurpArgs(self):
        parser = argparse.ArgumentParser(description='Provide parameter used to construct the gwa config file.')
        parser.add_argument("--OCService", help="openshift service that the route should bind to")
        parser.add_argument("--reponame", help="unique name for your smk app, usually the name of your repository.")
        parser.add_argument("--OCNamespace", help="The openshift namespace that the app resides in.")
        parser.add_argument("--servicePort", help="The port that the open shift service is configured for.")
        parser.add_argument("--kongDomain", help="The domain suffix that will be created.")
        parser.add_argument("--GWANamespace", help="the gwa namespace created using gwa tool")
        parser.add_argument("--GWAenv", help="the gwa namespace created using gwa tool")
        parser.add_argument("--endpointdir", help="the end point to add to your route", default='/')

        args = parser.parse_args()
        self.OCService = args.OCService
        self.reponame = args.reponame
        self.OCNamespace = args.OCNamespace
        self.servicePort = args.servicePort
        self.kongDomain = args.kongDomain
        self.GWANamespace = args.GWANamespace
        self.GWAenv = args.GWAenv
        self.endpointdir = args.endpointdir

    def createYaml(self):
        yamlData = \
            { 
                "_format_version": "1.1",
                "services": [
                    {
                        "name": self.OCService,
                        "host": f"{self.OCService}.{self.OCNamespace}.svc",
                        "port": int(f"{self.servicePort}"),
                        "tags": [
                            f"ns.{self.GWANamespace}.{self.reponame}", self.reponame, self.GWAenv
                        ],
                        "routes": [
                            {
                                'tags': 
                                [
                                    f"ns.{self.GWANamespace}.{self.reponame}", self.reponame, self.GWAenv
                                ],
                                'name': f"{self.reponame}-route",
                                "methods": [
                                    'GET' ],
                                "paths": [
                                    self.endPointDir],
                                "strip_path": False,
                                "hosts": [
                                    f"{self.reponame}.{self.kongDomain}"
                                ]
                            }
                        ]
                    }
                ]
            }
        yamlString = yaml.dump(yamlData, sys.stdout)



if __name__ == "__main__":

    # debug
    # sys.argv.append("smk-fap-fcp-svc")
    # sys.argv.append("smk-fap-fcb")
    # sys.argv.append("b16795-dev")
    # sys.argv.append("8888")
    # sys.argv.append("api.gov.bc.ca")
    # sys.argv.append("smk-apps")
    # sys.argv.append("dev")

    gwaConf = GWAConfig()
    gwaConf.slurpArgs()
    gwaConf.createYaml()
