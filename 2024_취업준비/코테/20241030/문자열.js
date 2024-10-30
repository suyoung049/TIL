var s = "Pyy"

function solution(s){
    let answer = true;
    let p_num = 0
    let y_num = 0

    length = s.length

    for (let i = 0; i < length; i++) {
        var new_s = s[i].toLowerCase()
        if (new_s === "p") {
            p_num += 1
        } 

        if (new_s === "y" ) {
            y_num += 1
        }
    }

    if (y_num !== p_num) {
        answer = false
    }


    return answer;
}

solution(s)