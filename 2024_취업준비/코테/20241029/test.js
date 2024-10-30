var num_list = [1, 2, 3, 4, 5]
var n = 3

function solution(num_list, n) {
    let answer = 0;
    var length = num_list.length
    for (let i = 0; i < length; i++) {
        if (num_list[i] === n) {
            answer = 1
        }
    }


    return answer;
}

solution(num_list, n)

