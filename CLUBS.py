cuisine_club = {"Arjun.J","Arjun.P","Navya","Aiden","Jullice"}
techdesign_club ={"Yuvan","Kanishk","Deera","Dhanyata","Arjun.J"}
both_clubs = cuisine_club.intersection(techdesign_club)
print (both_clubs)
alljoin = techdesign_club.union(cuisine_club)
print (alljoin)
diff = techdesign_club.difference(cuisine_club)
dif = cuisine_club.difference(techdesign_club)
print (diff,"and",dif)
sym = techdesign_club.symmetric_difference(cuisine_club)
print (sym)