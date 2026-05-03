class india:
    def feat(self,lang,curr,cap):
        print ("language is",lang)
        print ("currency  is",curr)
        print ("capital is",cap)
class USA:
    def feat(self,lang,curr,cap):
        print ("language is",lang)
        print ("currency  is",curr)
        print ("capital is",cap)
US = USA()
IN = india()
for country in(US,IN):
    country.feat()