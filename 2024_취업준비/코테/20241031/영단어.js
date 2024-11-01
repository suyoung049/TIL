function solution(s) {
    // 숫자 이름과 대응하는 객체
    const num_english = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    };

    // 정규 표현식으로 숫자 이름을 숫자로 변환
    for (const [key, value] of Object.entries(num_english)) {
        const regex = new RegExp(key, "g");  // key에 해당하는 패턴을 전역으로 찾음
        s = s.replace(regex, value); // key를 value로 대체
    }
    
    // 변환된 문자열을 숫자로 반환
    return parseInt(s, 10);
}

const s = "one4seveneight";
console.log(solution(s)); // 1478