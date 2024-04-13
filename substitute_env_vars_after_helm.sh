#!/bin/bash 
mv ./deployment_original.yaml ./shopilefthelm/templates/deployment.yaml 
mv ./values_original.yaml  ./shopilefthelm/values.yaml
mv ./configmap_original.yaml ./shopilefthelm/templates/configmap.yaml

# rm ./deployment_original.yaml 
# rm ./values_original.yaml
# rm ./configmap_originals.yaml

# rm  ./deployment_new.yaml
# rm  ./values_new.yaml
# rm  ./configmap_new.yaml