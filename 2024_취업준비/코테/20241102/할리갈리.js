const fs = require('fs');
const [n, ...input] = fs.readFileSync("3_input.txt", "utf-8").trim().split("\n");
// 숫자 n을 정수형으로 변환
const numItems = parseInt(n);


const fruit_dict = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}

for (let i = 0; i < numItems; i++) {
    [fruit, cnt] = input[i].split(" ")
    fruit_dict[fruit] += parseInt(cnt)
}

// 하나라도 값이 5 이상인 경우 "YES" 출력
if (Object.values(fruit_dict).some(value => value === 5)) {
    console.log("YES");
} else {
    console.log("NO");
}



