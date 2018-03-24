class SentimentAnalyzer:
    
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
        
        return label


    def average_sentiment(self,label):
        # sentiment analysis
        pos_review=0
        neg_review=0

        for x in label:
            if x==1:
                pos_review+=1

        neg_review = len(label)-pos_review
        pos_review_percent = (pos_review/float(len(label)))*100
        neg_review_percent = (neg_review/float(len(label)))*100

        return (pos_review_percent,neg_review_percent)



