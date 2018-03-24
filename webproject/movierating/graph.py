from movie import Movie

class GraphPlotter:

    def __init__(self,movie):
        self.movie = movie

    def get_label(self):
        user,reviews = self.movie.get_reviews()

        pos_words = ['liked','loved','awesome','nice','best','good','amazing','stunnning','incredible','enjoy','enjoyable','entertaining','marvellous','great','fantastic','outstanding']
        neg_words = ['bad','worse','worst','poor','unstatisfactory','unpleasant','terrible','awful','dislike','hate','lack','overrated','overhyped','nonsense']

        # sentiment analysis
        label=[]
        for sentence in reviews:
            pos=0
            neg=0
            sentence = sentence.strip().lower().split()
            for word in sentence:
                if(word in pos_words):
                    pos+=1
                elif(word in neg_words):
                    neg+=1
            if(pos>=neg):
                label.append(1)
            else:
                label.append(0)
        
        return (user,label)


    def gender_sentiment(self,label,gender):

        male_pos=0
        female_pos=0
        for i in range(len(label)):
            if(label[i]==1):
                if(gender[i]=='Male'):
                    male_pos+=1
                else:
                    female_pos+=1
        
        print(male_pos,female_pos)
        male_pos_percent = (male_pos/float(len(label)))*100
        female_pos_percent = (female_pos/float(len(label)))*100

        return male_pos_percent,female_pos_percent

    def age_sentiment(self,label,age):
        
        teen_pos=0
        young_pos=0
        old_pos=0
        for i in range(len(label)):
            if(label[i]==1):
                if(age[i]=='Teen'):
                    teen_pos+=1
                elif(age[i]=='Young'):
                    young_pos+=1
                else:
                    old_pos+=1
        teen_pos_percent = (teen_pos/float(len(label)))*100
        young_pos_percent = (young_pos/float(len(label)))*100
        old_pos_percent = (old_pos/float(len(label)))*100

        return (teen_pos_percent,young_pos_percent,old_pos_percent)
