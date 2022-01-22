import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) != 4:
    print("ERROR: Wrong number of arguments passed to script.\n"
          "Please call this script followed by the coach name, the old csv file path, and the new csv file path.\n"
          "Here is an example call:\n"
          "python3 coach_surveys.py \"Jonathan Stanley\" old_survey_responses.csv new_survey_responses.csv")
    sys.exit(0)

try:
    data = pd.read_csv(sys.argv[2], usecols=list(range(2, 3)) + list(range(4, 16)))
except FileNotFoundError as err:
    print(err)
    print(sys.argv[2], "does not exist in the directory indicated by the path you provided.\n"
          "Please check for typos. If there are none, please copy the csv file's pathname from\n"
          "the root and pass it as your csv argument:\n"
          "python3 coach_surveys.py \"Jonathan Stanhope\" /Users/bob/Documents/TalkMaze/survey_data.csv")
    sys.exit(0)
except pd.errors.EmptyDataError:
    print(sys.argv[2], "was empty. Please check your csv and make sure it contains data.\n")
    sys.exit(0)

x = data.loc[data['What is your coach\'s name?'] == sys.argv[1]]

num_values = len(x.columns)*len(x)
dict_copy = x.to_dict()

score = SA = A = N = D = SD = 0
scores = {"Strongly Agree": 5, "Agree": 4, "Neutral": 3, "Disagree": 2, "Strongly Disagree": 1}

for r in dict_copy:
    if r == 'What is your coach\'s name?':
        continue
    else:
        new_dict = dict_copy.get(r)
        key_arr = list(new_dict.keys())

        if len(key_arr) == 0:
            print("ERROR: Coach not found.\n"
                  "Please check for typos in the coach's name provided and review your data.\n"
                  "Also make sure the coach name is in quotes.\n"
                  "Here is an example call:\n"
                  "python3 coach_surveys.py \"Jonathan Stanley\" survey_responses.csv")
            sys.exit(0)

        for i in range(key_arr[0], key_arr[-1]+1):
            value = new_dict.get(i)
            if value == None:
                continue
            elif value == "Strongly Agree":
                SA += 1
            elif value == "Agree":
                A += 1
            elif value == "Neutral":
                N += 1
            elif value == "Disagree":
                D += 1
            else:
                SD += 1
            score += scores.get(value)


try:
    data2 = pd.read_csv(sys.argv[3], usecols=list(range(2, 3)) + list(range(4, 16)))
except FileNotFoundError as err:
    print(err)
    print(sys.argv[3], "does not exist in the directory indicated by the path you provided.\n"
          "Please check for typos. If there are none, please copy the csv file's pathname from\n"
          "the root and pass it as your csv argument:\n"
          "python3 coach_surveys.py \"Jonathan Stanhope\" /Users/bob/Documents/TalkMaze/survey_data.csv")
    sys.exit(0)
except pd.errors.EmptyDataError:
    print(sys.argv[3], "was empty. Please check your csv and make sure it contains data.\n")
    sys.exit(0)

x2 = data2.loc[data2['What is your coach\'s name?'] == sys.argv[1]]

num_values2 = len(x.columns)*len(x)
dict_copy2 = x2.to_dict()

score2 = SA2 = A2 = N2 = D2 = SD2 = 0

for r in dict_copy2:
    if r == 'What is your coach\'s name?':
        continue
    else:
        new_dict = dict_copy2.get(r)
        key_arr = list(new_dict.keys())

        if len(key_arr) == 0:
            print("ERROR: Coach not found.\n"
                  "Please check for typos in the coach's name provided and review your data.\n"
                  "Also make sure the coach name is in quotes.\n"
                  "Here is an example call:\n"
                  "python3 coach_surveys.py \"Jonathan Stanley\" survey_responses.csv")
            sys.exit(0)

        for i in range(key_arr[0], key_arr[-1]+1):
            value = new_dict.get(i)
            if value == None:
                continue
            elif value == "Strongly Agree":
                SA2 += 1
            elif value == "Agree":
                A2 += 1
            elif value == "Neutral":
                N2 += 1
            elif value == "Disagree":
                D2 += 1
            else:
                SD2 += 1
            score2 += scores.get(value)


score_arr = np.array([SA, A, N, D, SD])
score_arr_2 = np.array([SA2, A2, N2, D2, SD2])
type_arr = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
xpos = np.arange(len(type_arr))
plt.xticks(xpos, type_arr, fontsize=9)
plt.ylabel("Nbr. of student selections")
plt.title(sys.argv[1]+"'s Performance", color="#0A0C55", fontweight="bold")
plt.bar(xpos-0.2, score_arr, width=0.5, label="first survey", color="#62D3B3")
plt.bar(xpos+0.2, score_arr_2, width=0.5, label="second survey", color="#7564CD")
plt.legend()
plt.show()