curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
            unzip awscli-bundle.zip
            sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
			export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
			export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
			export AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION
			export AWS_DEFAULT_OUTPUT=json
			export PATH=/usr/local/aws:$PATH
			#aws configure $AWS_ACCESS_KEY_ID  $AWS_SECRET_ACCESS_KEY $AWS_DEFAULT_REGION $AWS_DEFAULT_OUTPUT
            aws iam delete-role --role-name aws_iam_role.lambda_exec_role
            aws lambda delete-function --function-name aws_lambda_function.My_airflow_request
