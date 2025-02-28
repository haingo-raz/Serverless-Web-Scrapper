import json
import boto3
from web_scraper import scrape_website

S3_BUCKET = "wikipediaonthisdaypfc710"

def lambda_handler(event, context):
    try:
        print("Starting web scraping...")
        today, json_filename, events, births, deaths = scrape_website()
        print(f"Scraped data for {today}. JSON file: {json_filename}")

        data = {today: {"events": events, "births": births, "deaths": deaths}}

        s3 = boto3.client('s3')
        try:
            print(f"Uploading data to S3 bucket: {S3_BUCKET}, file: {json_filename}")
            s3.put_object(
                Body=json.dumps(data, ensure_ascii=False, indent=4),
                Bucket=S3_BUCKET,
                Key=json_filename
            )
            print("Upload successful!")
        except Exception as e:
            print(f"Error uploading to S3: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps(f"Error uploading to S3: {e}")
            }

        return {
            'statusCode': 200,
            'body': json.dumps('Data successfully scraped and stored!')
        }

    except Exception as e:
        print(f"Error during web scraping: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error during web scraping: {e}")
        }