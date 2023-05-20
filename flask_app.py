from flask import Flask, render_template, request,redirect, url_for
from make_blank.high_level import blank_of_space_sents
from frontend.uder_bar_to_input import changing_under_par_to_input_tage
from result_texts import result_text


app = Flask(__name__)


@app.route("/")
def index():
  global blank_ids, unblanked_texts
  blank_ids=[]
  unblanked_texts=[]

  return render_template("index.html")



@app.route("/main",methods=["POST"])
def main():
    
    texts = request.form["texts"]
    try:
      print(unblanked_texts)
    except NameError:
      return redirect('/')
    # 차후 result에서 쓸 texts
    processed_texts=texts.split()
    for processed_text in processed_texts:
      if '.' in processed_text:
        processed_text=processed_text[:-1]
        unblanked_texts.extend([processed_text, '.'])
      else:
        unblanked_texts.append(processed_text)


    blank_persent=float(request.form["blank_persent"]) # 요기는 무조건 큰 따옴표여야 한다.
    having_blank_texts=blank_of_space_sents(texts, blank_persent=blank_persent)

    user_value=changing_under_par_to_input_tage(having_blank_texts)[0]
    # 입력 값을 처리합니다.
    blank_ids.extend(changing_under_par_to_input_tage(having_blank_texts)[1])
    
  
    post={'problem': f'{user_value}'}

    return render_template("main.html", post=post)


@app.route("/result", methods=["POST"])
def result():
  print(blank_ids)
  user_values={}
  for blank_id in blank_ids:
      try:
        user_values[blank_id]=request.form[f'value_{blank_id}']
      except KeyError:
        print('user values :',user_values, 'blank_ids',blank_ids)

  result, user_stendard=result_text(unblanked_text=unblanked_texts, user_values=user_values)
  correct_answer_num=user_stendard['정답 개수']
  wrong_answer_num=user_stendard['오답 개수']
  post={'body': f'<div>{result}</div>'}
  
  if not blank_ids:
    print('something is wrong.')
    return redirect('/')
  
  return render_template('result.html', post=post, correct_answer_num=correct_answer_num, wrong_answer_num=wrong_answer_num)



if __name__ == "__main__":
  app.run(host='127.0.0.1', port=8000, debug=True)
