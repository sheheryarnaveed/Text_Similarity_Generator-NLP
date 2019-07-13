# Text_Similarity_Generator-NLP
A text similarity generator tool that generates similarity score between two texts/documents. It currently supports both Chinese and English extracts

## Usage
- Clone the git repository
- Create a virtual env and install the required packages in requirements.txt `pip install -r requirements.txt`

## Terminal
```
python main.py [-h] [-c] [-e] [-s] -q

Required:
	-q The target enquiry with which to match
    
Optional:
	-c Path to the file containing chinese text
    -e Path to the file containing english text. Default filename is enquiries_dataset_english.csv
    -s A target score that determines how much similarity you want between texts. Default value is 1.0
    
	-h Help

```

