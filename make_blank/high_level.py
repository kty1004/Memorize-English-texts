import random
import nltk


def creat_blank(sent:str, blank_persent: float, result_list:list):
    seperated_words=sent.split() # 띄어쓰기 단위로 자름.
    '''blank 수 조절'''
    blank_number=int(len(seperated_words)*blank_persent)
    

    '''blank 단어 고르기'''
    random_words=[]
    now_blank_number=0
    while now_blank_number<=blank_number: # 생성한 빈칸 수가 설정한 빈칸의 수보다 작거나 같을 때까지만 작동함.
        random_word=seperated_words[random.randint(0,len(seperated_words)-1)]
        if random_word not in random_words:
            random_words.append(random_word)
            now_blank_number+=1


    '''create blank'''
    
    #creat_blank(seperated_words=seperated_words, result_list=result_sents, random_words=random_words)
    for seperated_word in seperated_words:
        if seperated_word in random_words:
            if '.' in seperated_word: # 만약 랜덤 단어에 .(마침표)가 있을 때
                result_list.extend(['_'*(len(seperated_word)-1),'.'])
            else:
                result_list.append('_'*len(seperated_word))
        else:
            result_list.append(seperated_word)


def blank_of_space_sents(user_texts, blank_persent): # 빈 칸 수 조절
    # 빈 칸 수 조절은 %으로 한다.
    if blank_persent>=1:
        print(f'blank persent could not be {blank_persent}. plz setting blank persent under 1')
    else:
        sents=nltk.sent_tokenize(user_texts) # 문장 단위로 자름.
        result_sents=[]
        for sent in sents: # 글을 문장으로 쪼갬.
            creat_blank(sent=sent, blank_persent=blank_persent, result_list=result_sents)
            
        result_sents=" ".join(result_sents)

        return result_sents

def blank_of_space_sent(user_texts, blank_persent):
    if blank_persent>=1:
        print(f'blank persent could not be {blank_persent}. plz setting blank persent under 1')
    else:
        result_sent=[]

        sents=nltk.sent_tokenize(user_texts) # 문장 단위로 자름.
        random_sent=random.choice(sents)
        creat_blank(sent=random_sent, result_list=result_sent, blank_persent=blank_persent)
        result_sent=" ".join(result_sent)
        return result_sent
