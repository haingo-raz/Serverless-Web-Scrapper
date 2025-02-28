import json
import boto3
from web_scrapper import scrape_website

S3_BUCKET = "wikipediaonthisdaypfc710"

def lambda_handler(event, context):
    today, json_filename, events, births, deaths = scrape_website()
    
    s3 = boto3.client('s3')
    data = {today: {"events": events, "births": births, "deaths": deaths}}
    s3.put_object(
        Body=json.dumps(data, ensure_ascii=False, indent=4),
        Bucket=S3_BUCKET, 
        Key=json_filename
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data successfully scraped and stored!')
    }