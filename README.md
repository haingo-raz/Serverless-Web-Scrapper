# About
This project is a web scraper created with Python and AWS that displays events that happened on today's date. The content will be updated daily to reflect the current date. Users will also be able to access previously scraped "on this day" articles.

# Installation
1. Make sure you have the [AWS CLI](https://aws.amazon.com/cli/) installed.
2. Create a virtual environment to run the project. To install all the dependencies, run:
   ```sh
   pip install -r requirements.txt
   ```
3. Create an S3 bucket with a unique name where the JSON results from the web scraping will be stored. Make the S3 bucket publicly accessible and add the policy below to make the objects accessible:
   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
         {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-unique-bucket-name/*"
         }
      ]
   }
   ```
4. Package the `lambda_function.py` file with the `web_scraper.py` file along with the installed libraries, and upload it to AWS Lambda using Python as the runtime. Make sure to also increase the timeout duration of the Lambda function.
5. Create a new rule on AWS EventBridge to trigger the Lambda function at a specific time/interval.
6. Create a static HTML file to fetch the JSON files uploaded in the S3 bucket. The HTML file will be accessible from the S3 bucket's public URL.