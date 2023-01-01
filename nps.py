import numpy as np

print("Welcome to NET PROMOTER SCORE calculator:")
scores=np.loadtxt('survey.txt',dtype='int')
print("Here is the complete date set:",scores)
print("The number of respondents are:",len(scores))
print("The maximum score received is:",scores.max())
print("The minimum score received is:",scores.mean())

#detractors
detractors=scores[scores<7]
print("The number of detractors are:",len(detractors))

promoters=scores[scores>8]
print("The number of promoters are:",len(promoters))

nps=100*(len(promoters)-len(detractors))/len(scores)
print("NET PROMOTER SCORE is:",nps)


