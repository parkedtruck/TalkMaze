pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys


if len(sys.argv) != 2:
    print("ERROR: Wrong number of arguments passed to script.\n"
          "Please call this script followed by the coach name, the old csv file path, and the new csv file path.\n"
          "Here is an example call:\n"
          'python3 coach_surveys.py "Jonathan Stanley" old_survey_responses.csv new_survey_responses.csv')
    sys.exit(0)

print(sys.argv[1])

try:
    data = pd.read_csv(sys.argv[1], usecols=list(range(4, 16)))
except FileNotFoundError as err:
    print(err)
    print(sys.argv[1], "does not exist in the directory indicated by the path you provided.\n"
          "Please check for typos. If there are none, please copy the csv file's pathname from\n"
          "the root and pass it as your csv argument:\n"
          'python3 coach_surveys.py "Jonathan Stanhope" /Users/bob/Documents/TalkMaze/old_survey.csv new_survey.csv')
    sys.exit(0)
except pd.errors.EmptyDataError:
    print(sys.argv[2], "was empty. Please check your csv and make sure it contains data.\n")
    sys.exit(0)

ind_list = [0,1,2,3,4,5,7,8,9,10,11,12,15,16,19,20,21,22,24,25,26,28,29,30]
ndata = data.iloc[ind_list]

num_values = len(ndata.columns)*len(ndata)

dict_copy = ndata.to_dict()

score = SA = A = N = D = SD = 0
score3 = SA3 = A3 = N3 = D3 = SD3 = 0
scores = {"strongly agree": 5, "agree": 4, "neutral": 3, "disagree": 2, "strongly disagree": 1}


score_one = {}
for r in dict_copy:
    #if r == 'What is your coach\'s name?':
    #    continue
    #else:
    new_dict = dict_copy.get(r)
    key_arr = list(new_dict.keys())
    the_score = 0
    for i in key_arr:

        value = new_dict.get(i).lower()
        if value is None:
            continue
        elif value == "strongly agree":
            SA += 1
            SA3 += 1
        elif value == "agree":
            A += 1
            A3 += 1
        elif value == "neutral":
            N += 1
        elif value == "disagree":
            D += 1
        else:
            SD += 1

        the_score += scores.get(value)
        score += scores.get(value)

        score_one[r] = the_score


print(score_one)


ind_list2 = [37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 61, 62, 63, 64, 65]
ndata2 = data.iloc[ind_list2]


num_values2 = len(ndata2.columns)*len(ndata2)
dict_copy2 = ndata2.to_dict()

print(num_values2)

score2 = SA2 = A2 = N2 = D2 = SD2 = 0

score_dist = {}

for r in dict_copy2:

    new_dict = dict_copy2.get(r)
    key_arr = list(new_dict.keys())
    this_score = 0
    for i in key_arr:
        value = new_dict.get(i).lower()
        if value == None:
            continue
        elif value == "strongly agree":
            SA2 += 1
        elif value == "agree":
            A2 += 1
        elif value == "neutral":
            N2 += 1
        elif value == "disagree":
            D2 += 1
        else:
            SD2 += 1
        this_score += scores.get(value)
        score2 += scores.get(value)

        score_dist[r] = this_score

print(score2)

print(score_dist)



'''
score_arr = np.array([SA, A, N, D, SD])
score_arr_2 = np.array([SA2, A2, N2, D2, SD2])
type_arr = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
xpos = np.arange(len(type_arr))
plt.xticks(xpos, type_arr, fontsize=9)
plt.ylabel("Nbr. of student selections")
plt.title("Debate Performance Nov 2021 - Jan 2022", color="#0A0C55", fontweight="bold")
plt.bar(xpos-0.2, score_arr, width=0.5, label="first survey", color="#62D3B3")
plt.bar(xpos+0.2, score_arr_2, width=0.5, label="second survey", color="#7564CD")
plt.legend()
plt.show()
'''

score_arr = np.array([SA, A, N, D, SD])
score_arr_2 = np.array([SA2, A2, N2, D2, SD2])
type_arr = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
xpos = np.arange(len(type_arr))
plt.xticks(xpos, type_arr, fontsize=9)
plt.ylabel("Nbr. of student selections")
plt.title("Debate Performance Nov 2021 - Jan 2022", color="#0A0C55", fontweight="bold")
plt.bar(xpos-0.2, score_arr, width=0.5, label="first survey", color="#62D3B3")
plt.bar(xpos+0.2, score_arr_2, width=0.5, label="second survey", color="#7564CD")
plt.legend()
plt.show()
