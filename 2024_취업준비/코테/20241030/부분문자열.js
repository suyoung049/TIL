var t = "10203"
var p = "15"

function solution(t, p) {
    var answer = 0;

    length = t.length
    p_length = p.length
    

    for (let i = 0; i < length + 1 - p_length; i++) {
        var str_num = ""
        for (let j = i; j < i+ p_length; j++) {
            str_num += t[j]
        }
        if (Number(str_num) <= Number(p)) {
            answer += 1
        }
    }

    return answer;
}

(solution(t, p))

