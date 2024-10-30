var s = "aaabbaccccabba"

function solution(s) {
    var text_list = []
    var answer = 0;
    length = s.length
    var s_cnt = 0
    var cnt = 0

    for (let i=0; i <length; i++) {
        text_list.push(s[i])

        if (text_list[0] === s[i]) {
            s_cnt += 1
        } else {
            cnt += 1
        }

        if (s_cnt === cnt) {
            
            answer += 1
            s_cnt = 0
            cnt = 0
            text_list = []
        } else if ( i === length -1) {
            answer += 1
        }

    }

    return answer;
}

solution(s)