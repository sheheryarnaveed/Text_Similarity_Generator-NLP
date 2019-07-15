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
    	-s A target score that determines how much similarity you want between texts. Default value is 0.5
    
	-h Help

```

### For example the following commands would work:

- `python main.py -s 1.5 -q October` => where the targetScore = "1.5" and query="October"
- `python main.py -s 6.5 -q Hello -c enquiry_similarity_set.csv` => where the targetScore = "6.5" and query="October" and Chinese text file = "enquiry_similarity_set.csv"
- `python main.py -s 2.8 -q "How are you?" -e enquiries_dataset_english.csv` => where the targetScore = "2.8" and query="How are you?" and English text file = "enquiries_dataset_englisht.csv"

### Output

- `41  ,  0.5797386715376657  =>  Will there be a lecture in October?` where 41 is the row number in csv file and ~0.58 is similarity confidence score and "Will there be a lecture in October?" is the text found similar to the given test enquiry.

