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

    def setService(self, serviceName):
        self.service = serviceName

    def setSilverUrl(self, url):
        self.silverUrl = url

    def setGWANamespace(self, namespace):
        self.namespace = namespace

    def setEndPointPath(self, endPointDir):
        self.endPointDir = endPointDir

    def setGWARouteName(self, routeName):
        self.routeName = routeName

    def setNewUrlPrefix(self, prefix):
        self.destUrlPrefix = prefix

    def slurpArgs(self):
        parser = argparse.ArgumentParser(description='Provide parameter used to construct the gwa config file.')
        parser.add_argument("service", help="openshift service that the route should bind to")
        parser.add_argument("ocUrl", help="openshift route to your app, likely a apps.silver.devops.gov.bc.ca url")
        parser.add_argument("gwa_namespace", help="the gwa namespace created using gwa tool")
        parser.add_argument("gwa_route_name", help="name of the gwa route that will be created")
        parser.add_argument("url_prefix", help="will be appended on to the start of the url to make it unique")
        parser.add_argument("--endpointdir", help="the end point to add to your route", default='/')
        args = parser.parse_args()
        self.setService(args.service)
        self.setSilverUrl(args.ocUrl)
        self.setGWANamespace(args.gwa_namespace)
        self.setGWARouteName(args.gwa_route_name)
        self.setNewUrlPrefix(args.url_prefix)
        self.setEndPointPath(args.endpointdir)

    def createYaml(self):
        yamlData = \
            { 
                "_format_version": "1.1",
                "services": [
                    {
                        "name": self.service,
                        "url": self.silverUrl,
                        "plugins": [],
                        "tags": [
                            'OAS3_import', f"ns.{self.namespace}"
                        ],
                        "routes": [
                            {
                                'tags': 
                                [
                                    "OAS3_import", f"ns.{self.namespace}"
                                ],
                                'name': self.routeName,
                                "methods": [
                                    'GET' ],
                                "paths": [
                                    self.endPointDir],
                                "strip_path": False,
                                "hosts": [
                                    self.destUrlPrefix
                                ]
                            }
                        ]
                    }
                ]
            }
        yamlString = yaml.dump(yamlData, sys.stdout)
        #print(yamlString)



if __name__ == "__main__":

    # debug
    # sys.argv.append("smk-fap-fcp-svc")
    # sys.argv.append("https://smk-fap-fcb-rt-b16795-dev.apps.silver.devops.gov.bc.ca/")
    # sys.argv.append("smk-apps")
    # sys.argv.append("smk-fap-fcp-kong-route")
    # sys.argv.append("smk-fap-fcb")


    gwaConf = GWAConfig()
    gwaConf.slurpArgs()
    gwaConf.createYaml()
