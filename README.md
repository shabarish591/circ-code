# Circle CI Sample

This is a sample NodeJS project that uses CircleCI 2 and terraform to deploy a simple REST API using AWS API Gateway and a Lambda.

## Deploying

1. Fork the repo
2. Modify the `variables.tf` file in the pipeline folder (otherwise there may be conflicts between multiple deploys to the same account)
  - Change the defaults for lambda_name, api_gateway_name and role_name to something unique
  - Change the key in the backend to something unique: ie. circle_demo_username 
  - Commit your changes
3. Login to circle and connect your github account http://circleci2-poc.baat.nikecloud.com/
4. Select **Projects** and then your name, or org that you cloned the repo into
5. Select the **Build Project** button on the right of the Sample_Circle project (this build will fail because we haven't entered our credentials yet)
6. Click the project settings button at the top right (gear icon :gear:)
7. On the left click **AWS Permissions**
8. Enter your **Access Key Id** and **Secret Access Key** and click **Save**
9. Click **View sample_circle**
10. On the failed build Click **rebuild**


## Using
A successful build will give you an invokeUrl to the newly created APIGateway endpoint, to find it:

1. Click into a successful build
2. Click on the final step of the build to see the console output
3. At the bottom of the output you will see a URL like: `display_invoke_url = Invoke URL: https://nzklondagg.execute-api.us-west-2.amazonaws.com/dev/{proxy+}`
4. Navigate to the url in your browser and you will get a response like following:
```json
    {
        "message": "hello lambda",
        "path": "/test"
    }
```

Note: you can replace {proxy+} with any path you want in the url and it will return the path you enter in the body


## Destroying
To destroy the infrastructure you deployed you will need Terraform 0.10 and the AWS CLI installed locally

1. `cd circle_demo/pipeline`
2. run `terraform init` to connect to the remote s3 backend
3. run `terraform destroy` and type yes to initiate the destroy
