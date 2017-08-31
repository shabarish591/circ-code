#!/bin/bash

cd $1
DEP_PKG_DIR="ngp_automation_switchboard"

if [ -f "lambda_deploy"/${DEP_PKG_DIR}.zip ]; then
  mkdir -p lambda_deploy
  cp -rf circ-code lambda_deploy
  cd lambda_deploy
  mkdir -p ${DEP_PKG_DIR}
  mkdir py_dep
  virtualenv -q py_dep_env
  source py_dep_env/bin/activate; pip -q install -r circ-code/requirements.txt; deactivate
  cp -a py_dep_env/lib/python2.7/site-packages/. py_dep
  if [ -d "py_dep_env/lib64" ]; then
    cp -a py_dep_env/lib64/python2.7/site-packages/. py_dep
  fi
  if [ -d "py_dep_env/src" ]; then
    cp -a py_dep_env/src/. py_dep
  fi
  cp -rf circ-code ${DEP_PKG_DIR}
  rm -rf ${DEP_PKG_DIR}/circ-code/.git
  rm -f ${DEP_PKG_DIR}/circ-code/.gitignore
  cp -a py_dep/. ${DEP_PKG_DIR}
  cp circ-code/lambda_functions/switchboard.py ${DEP_PKG_DIR}
  cd ${DEP_PKG_DIR}; zip -qr9 ../${DEP_PKG_DIR}.zip .
fi
