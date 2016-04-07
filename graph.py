import numpy as np
import matplotlib.pyplot as plt
from statistics import mode, mean

first = []
second = []
third = []

with open("presentation.txt") as f:
    first = f.readlines()

with open("project.txt") as f:
    second = f.readlines()

with open("normalised.txt") as f:
    third = f.readlines()


# Remove exchange student marks
for i in range(0, len(third)):
    if len(third)>i:
        if float(third[i])>30:
            del first[i]
            del second[i]
            del third[i]

for i in range(0, len(second)):
    if len(second)>i:
        if float(second[i])>30:
            del first[i]
            del second[i]
            del third[i]



first_per = lambda y: (int(y)/60)*100
second_per = lambda y: (float(y)/40)*100
third_per = lambda y: (float(y)/30)*100

first_noper = first
first = list(map(first_per, first_noper))

second_noper = second
third_noper = third

second =list( map(second_per, second_noper))
third = list(map(third_per, third_noper))


average_presentation = mean(first)
mode_presentation = mode(first)


average_project = mean(second)
mode_project = mode(second)

average_normalised = mean(third)
mode_normalised = mode(third)

# Presentation
plt.figure(1)
#plt.subplot(211)
plt.ylabel('Number of people')

plt.xlabel("Percentage mark for presentation")
plt.text(65, 15, "Mean percentage: " + str(int(average_presentation)))
plt.text(65, 14, "Mode percentage: " + str(int(mode_presentation)))

plt.hist(sorted(first))
plt.axis([0,100,0,20])


# Project Mark
plt.figure(2)
#plt.subplot(221)
plt.text(20, 15, "Mean percentage: " + str(int(average_project)))
plt.text(20, 14, "Mode percentage: " + str(int(mode_project)))

plt.hist(sorted(second))
plt.axis([0,100,0,20])
plt.ylabel('Number of people')

plt.xlabel("Percentage mark for project")



# Normalised
plt.figure(3)
#plt.subplot(121)
plt.text(20, 15, "Mean percentage: " + str(int(average_normalised)))
plt.text(20, 14, "Mode percentage: " + str(int(mode_normalised)))

plt.hist(sorted(third))
plt.ylabel('Number of people')
plt.xlabel("Percentage mark for normalised")
plt.axis([0,100,0,20])
plt.show()

