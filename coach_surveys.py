import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

colns = list(range(2, 3)) + list(range(4, 16))
data = pd.read_csv(sys.argv[2], usecols=colns)

x = data.loc[data['What is your coach\'s name?'] == sys.argv[1]]

num_values = len(x.columns)*len(x)
dict_copy = x.to_dict()

score = SA = A = N = D = SD = 0
scores = {"Strongly Agree": 4, "Agree": 3, "Neutral": 2, "Disagree": 1, "Strongly Disagree": 0}

for r in dict_copy:
    if r == 'What is your coach\'s name?':
        continue
    else:
        new_dict = dict_copy.get(r)
        key_arr = list(new_dict.keys())

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

print("Strongly Agree:",SA,"\nAgree:", A,"\nNeutral:", N,"\nDisagree:", D,"\nStrongly Disagree:", SD)
print("Score:", (score/(num_values*4))*100)
score_arr = np.array([SA, A, N, D, SD])
plt.pie(score_arr)
plt.legend(["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"], bbox_to_anchor=(0.80, 0.80))
plt.show()