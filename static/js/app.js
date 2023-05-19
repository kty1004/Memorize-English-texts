
function autoResize() {
    const textarea = document.getElementById("myInput");
    
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
}
function clearText(){
    str="여기에 본문을 입력하세요."
    const textarea = document.getElementById("myInput");
    textareaValue=textarea.value.trim()
    if (textareaValue == str) {
        textarea.value = "";
    }
}

function fillText(){
    const textarea = document.getElementById("myInput");
    textareaValue=textarea.value.trim()
    if (textareaValue == "") {
        textarea.value = "여기에 본문을 입력하세요.";
    }
}


// 폼 제출 방지

document.querySelector("form").addEventListener("submit", function(event) {
    const regex = /^[\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F\uA960-\uA97F\uAC00-\uD7A3]*$/;
    const input = document.getElementsByTagName('textarea');
    const value=event.target.querySelector('textarea').value
    if (value === "여기에 본문을 입력하세요.") {
        event.preventDefault();
        alert('본문을 입력하고 다음 페이지로 넘어갈 수 있습니다!!!')
    } else if (regex.test(value)) {
        const result= confirm('한글이 감지되었습니다. 그대로 진행을 할까요?')
        if (result) {
            document.querySelector("form").submit()
        }else {
            event.preventDefault()
        }
    }
    console.log(value)
});


