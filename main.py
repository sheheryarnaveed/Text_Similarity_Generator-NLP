from textParser import deEmojify
from cosineSimilarity import cosine_sim
import pandas as pd
import time
from mtranslate import translate
import textwrap
import sys
import argparse

parser = argparse.ArgumentParser(
    description='A text similarity generator tool that generates similarity score between two texts/documents. It currently supports both chinese and english extracts'
)
parser.add_argument('-e', dest='efile', help="Path to the file containing english text", default='./enquiries_dataset_english.csv')

parser.add_argument('-c', dest='cfile', help="Path to the file containing chinese text")

parser.add_argument('-s', dest='targetscore', help="A target score that determines how much similarity you want between texts", default=1.0)

parser.add_argument('-q', dest='query', help="The target enquiry with which to match", required=True)

args = parser.parse_args()

query = args.query

if(args.cfile):
    try:
        df = pd.read_csv(args.cfile)
        for index, row in df.iterrows():
            translated_text = ""
            if(len(deEmojify(row['Enquiry'])) > 2200):
                print("inside")
                sep_data = textwrap.wrap(deEmojify(row['Enquiry']), 2000)
                for i in range(0, len(sep_data)):
                    translated_text += translate(deEmojify(sep_data[i]), "en", "auto")
            else:
                translated_text = translate(deEmojify(row['Enquiry']), "en", "auto")
            similarity = cosine_sim(translated_text, query)
            if(similarity > float(args.targetscore)):
                print(similarity, " => " , translated_text)
    except:
        print("Sorry, something went wrong while generating scores from csv file %(filename)s!" % {"filename" : args.cfile})
else:
    try:
        df = pd.read_csv(args.efile, engine='python')
        for index, row in df.iterrows():
            processed_data = deEmojify(row['Enquiry'])
            similarity = cosine_sim(processed_data, query)
            if (similarity > float(args.targetscore)):
                print(index+2, " , ", similarity, " => ", processed_data)
    except:
        print("Sorry, something went wrong while generating scores from csv file %(filename)s!" % {"filename": args.efile})



print("Processing Finished!")


