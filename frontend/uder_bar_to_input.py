def changing_under_par_to_input_tage(texts):
    form_tag=f'<form  action="/result" method="post" />'
    result=[form_tag]
    seperated_words=texts.split() # 띄어쓰기 단위로 자름.
    blank_id=[]
    for num in range(len(seperated_words)):
        if '_' in seperated_words[num]:
            blank_id.append(int(num))
            result.append(f'<input pattern="^\S+$" title="띄어쓰기 금지!!" type=texts id={int(num)} name=value_{int(num)} required />') # id는 특정 번째 단어를 말함.
        else:
            result.append(seperated_words[num])
    
    # create submit button
    button_tag='<div class=center_column ><input type="submit" value="확인" class="button"></div>'
    result.extend([button_tag, '</form>'])
    result=' '.join(result)
    return result, blank_id
