# About
Web Scraper created with Python and AWS that displays events that happened on today's date. The content will be updated every single day to reflect the current date. Users should be able to access previously scraped "on this day" articles.

# Installation
1. Make sure you have [AWS CLI](https://aws.amazon.com/cli/) installed.

# Components
1. Web Scraper that scrapes a list of events that happened on today's date.

2. Packaging the Python files with libraries
    - Activate the virtual environment:
      - Windows:
         ```
         venv\Scripts\activate
         ```
      - macOS/Linux:
         ```
         source venv/bin/activate
         ```

    - Install required packages:
      ```
      pip install -r requirements.txt
      ```

    - Locate installed dependencies:
      - Windows:
         ```
         venv/Lib/site-packages/
         ```
      - macOS/Linux:
         ```
         venv/lib/pythonX.X/site-packages/
         ```

    - Copy dependencies for packaging:
      - Windows (PowerShell):
         ```
         mkdir package
         Copy-Item -Recurse venv\Lib\site-packages\* package\
         ```
      - macOS/Linux:
         ```
         mkdir package
         cp -r venv/lib/python*/site-packages/* package/
         ```

    - Add the Lambda function files:
      ```
      cp lambda_function.py package/
      cp web_scraper.py package/
      ```

    - Zip everything:
      - Windows:
         ```
         Compress-Archive -Path package\* -DestinationPath lambda_function.zip
         ```
      - macOS/Linux:
         ```
         cd package
         zip -r ../lambda_function.zip .
         cd ..
         ```

3. Create an S3 bucket where the JSON files will be stored.

# Wikipedia
- On this day: [Wikipedia Main Page](https://en.wikipedia.org/wiki/Main_Page)