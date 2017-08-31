
terraform {
  backend "s3" {
    bucket   = "serverless-lambda-b"
    key      = "nike-lambda/terraform.tfstate"
    region   = "us-west-2"
  }
}

resource "aws_s3_bucket" "my-nike-lambda-bucket" {
  bucket = "my-nike-lambda-bucket"
  acl    = "private"

  tags {
    Name        = "my-nike-lambda-bucket"
    Environment = "Dev"
  }
}
variable "stage" {
  default = "Dev"
}
variable "lambda_file" {
  default = "../pipeline/lambda.zip"
}
