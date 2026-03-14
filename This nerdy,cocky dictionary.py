cocky_dict = {'aadi': '49','anirved':'49','bhargav':'50','yuvan:':'48'}
K = '49'
count = 0
for key in cocky_dict:
    if cocky_dict[key] == K:
        count = count + 1
print (count)
for key,values in cocky_dict.items():
    print (key,"=",values)