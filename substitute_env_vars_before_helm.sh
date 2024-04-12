#!/bin/bash 

cp shopilefthelm/templates/deployment.yaml ./deployment_original.yaml

envsubst < ./shopilefthelm/templates/deployment.yaml > ./deployment_new.yaml

mv ./deployment_new.yaml ./shopilefthelm/templates/deployment.yaml

cp shopilefthelm/values.yaml ./values_original.yaml

envsubst < ./shopilefthelm/values.yaml > ./values_new.yaml

mv ./values_new.yaml ./shopilefthelm/values.yaml

cp shopilefthelm/templates/configmap.yaml ./configmap_original.yaml

envsubst < ./shopilefthelm/templates/configmap.yaml > ./configmap_new.yaml

mv ./configmap_new.yaml ./shopilefthelm/templates/configmap.yaml






