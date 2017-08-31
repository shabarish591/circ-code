#!/bin/bash
# Run this from the project root
set -e

npm run build

ENVIRONMENT=${1}
echo "Running tf-deploy on ${ENVIRONMENT}"

pushd pipeline/terraform
terraform init
terraform workspace select ${ENVIRONMENT}
terraform apply
popd

# The site doesn't get deployed by terraform, because
npm run deploy:${ENVIRONMENT}
