import pandas as pd
import re

def findWholeWord(w):
	# https://cloud.tencent.com/developer/ask/45187
	return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

df = pd.read_excel("records.xls")

# the following part print the abstract
with open("PrintAbstracts.md", "w+") as f:
	for i in range(0, len(df["Abstract"])):
		print("### "+str(i+1)+". {0}".format(df['Article Title'][i]), file=f)
		print("1. "+"{0}".format(df['Author Full Names'][i]), file=f)
		print("2. "+"{0}".format(df['Journal Abbreviation'][i]), file=f)
		print("> "+"{0}".format(df['Abstract'][i]), file=f)

# the following find out th number of specific keywords
numOfAssignment = 0
with open("assignment.md", "w+") as f:
	for i in range(0, len(df["Author Keywords"])):
		if (len(str(df["Author Keywords"][i])) > 5):
			if findWholeWord("assignment")(df["Author Keywords"][i]) or findWholeWord("transit assignment")(df["Author Keywords"][i]) or findWholeWord("traffic assignment")(df["Author Keywords"][i]) or findWholeWord("equilibrium")(df["Author Keywords"][i]):
				numOfAssignment = numOfAssignment + 1
				print("### "+str(i+1) +
					  ". {0}".format(df['Article Title'][i]), file=f)
				print("1. "+"{0}".format(df['Author Full Names'][i]), file=f)
				print(
					"2. "+"{0}".format(df['Journal Abbreviation'][i]), file=f)
				print("> "+"{0}".format(df['Abstract'][i]), file=f)

print("Num of Assignment = {0}".format(numOfAssignment))
