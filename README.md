# DevEx Surveys to Excel #
This script takes the DevEx surveys found at https://docs.port.io/guides/all/create-surveys#set-up-a-survey-action and converts them all into a tabular Excel spreadsheet for reuse.

## How does it work? ##
The `surveys` folder contains the JSON object for each of the survey actions as per the guide above. The script will loop through the folder and extract each survey into a tab within the spreadsheet. If the surveys are updated or added, simply put them into the `surverys` folder and the script will parse them into the spreadsheet.

## What does it create? ##
A spreadsheet `all_surveys.xlsx` in the same directory that the script is run

## To Run ##
```
pip install -r requirements.txt
python main.py
```