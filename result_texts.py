def result_text(unblanked_text: list, user_values:dict):
    blank_ids=list(user_values.keys()) # blank의 인덱스를 리스트로 저장.
    wrong_texts_num=0
    corret_texts_num=0
    for blank_id in blank_ids:
        if unblanked_text[blank_id]==user_values[blank_id]: # 정답인 경우 글자 색을 파란색으로 한다.
            unblanked_text[blank_id]=f'<span class=correct-text>{user_values[blank_id]}</span>'
            corret_texts_num+=+1
        else: # 오답인 경우 글자색을 빨간색으로 처리
            unblanked_text[blank_id]=f'<span class=wrong-text>{user_values[blank_id]}</span>'
            wrong_texts_num+=+1
    unblanked_text=' '.join(unblanked_text)

    user_memorize_standard={'정답 개수':corret_texts_num, '오답 개수':wrong_texts_num}
    return unblanked_text, user_memorize_standard

