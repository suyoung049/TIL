const fs = require('fs');
const [n, ...input] = fs.readFileSync("2_input.txt", 'utf-8').replace(/\r/g, '').trim().split("\n");


// 숫자 n을 정수형으로 변환
const numItems = parseInt(n);
const password = {}


for (let i=0; i < numItems; i++) {
    reverse_word = ""
    word = input[i]
    for (let j= word.length -1; j >=0; j--) {
        reverse_word += word[j]
    }
    password[word] = reverse_word
}

let answer = ""

for (let key in password) {
    if (input.includes(password[key])) {
        answer = password[key]
        break
    }
}


const mid = Math.floor(answer.length / 2)
console.log(answer.length, answer[mid])
