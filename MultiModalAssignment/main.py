import pandas as pd
import re

"""Remark: the excel file was checked, so the number should be less the origin excel
"""


def findWholeWord(w):
	# https://cloud.tencent.com/developer/ask/45187
	return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


df = pd.read_excel("records.xls")


# tt = df['Article Title']
abs = df["Abstract"]
# print(df['Abstract'][0])
if findWholeWord("sustainable")(df["Abstract"][0]):
	print("find sustainable")
if findWholeWord("nable")(df["Abstract"][0]):
	print("find able")
# if "sustainable" in df["Abstract"][0]:
#     print("find word")

# ------------------------------------------
# the following part print the abstract
with open("PrintAbstracts.md", "w+") as f:
	for i in range(0, len(df["Abstract"])):
		print("### "+str(i+1)+". {0}".format(df['Article Title'][i]), file=f)
		print("1. "+"{0}".format(df['Author Full Names'][i]), file=f)
		print("2. "+"{0}".format(df['Journal Abbreviation'][i]), file=f)
		print("> "+"{0}".format(df['Abstract'][i]), file=f)
# ------------------------------------------
# check number of variaional inequality
# numOfVI = 0
# for i in range(0,len(df["Abstract"])):
#     if (len(str(df["Abstract"][i])) >10): # remark: one record abstract is na
#         if findWholeWord("vi")(df["Abstract"][i]):
#             numOfVI = numOfVI + 1
#         elif findWholeWord("variationl inequality")(df["Abstract"][i]):
#             numOfVI = numOfVI + 1
# print("Num of Vi = {0}".format(numOfVI))


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
		# elif findWholeWord("variationl inequality")(df["Author Keywords"][i]):
		#     numOfAssignment = numOfAssignment + 1
print("Num of Assignment = {0}".format(numOfAssignment))
