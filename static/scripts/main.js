function clearOldSelectDiv(){
    const el = document.querySelectorAll('.char_message_in_select')
    el.forEach((element) => element.className = "char_message_in")
}
async function select_char(o){
    await clearOldSelectDiv();

    const list = document.getElementsByName(o.id)

    list.forEach((element) => {
        element.className = 'char_message_in_select';
    })   
}
function setCharToSelectedDiv(str){
    const el = document.querySelectorAll('.char_message_in_select')
    el.forEach((element) => {
        element.innerHTML = str;
    })
}

document.onkeyup = function(evt) {
    const allowChars = "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
    if (allowChars.indexOf(evt.key) <= -1){
        return
    }else{
        setCharToSelectedDiv(evt.key)
    }
};