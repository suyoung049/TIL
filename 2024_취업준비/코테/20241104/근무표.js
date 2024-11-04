const fs = require('fs');
const [n, ...input] = fs.readFileSync(0, 'utf-8').trim().split("\n");

// 숫자 n을 정수형으로 변환
const numItems = parseInt(n);

// 입력 데이터를 2차원 배열로 변환
const listOfLists = input.map(line => line.split(" ").map(word => word.trim()));

const time_table = {}

// 근무 시간대별 시간 설정
const shiftHours = [4, 6, 4, 10]; // shift 0, 1, 2, 3

for (let week = 0; week < numItems; week++) {
    // 각 주마다 4개의 시간대에 대한 데이터를 저장
    const weekShifts = [];
    for (let shift = 0; shift < 4; shift++) {
        const shiftIndex = week * 4 + shift;
        weekShifts.push(listOfLists[shiftIndex]);
    }

    // 각 주의 7일을 순회
    for (let day = 0; day < 7; day++) {
        // 해당 날짜에 근무자가 있는지 확인
        let dayHasWorkers = false;
        for (let shift = 0; shift < 4; shift++) {
            if (weekShifts[shift][day] !== '-') {
                dayHasWorkers = true;
                break;
            }
        }

        // 날짜별로 4개의 시간대 모두 근무자가 있거나 없다는 조건 처리
        if (dayHasWorkers) {
            // 모든 시간대에 대해 근무자를 처리
            for (let shift = 0; shift < 4; shift++) {
                const worker = weekShifts[shift][day];
                if (worker === '-') continue; // 근무자가 없는 경우 넘어감

                const time = shiftHours[shift];
                if (worker in time_table) {
                    time_table[worker] += time;
                } else {
                    time_table[worker] = time;
                }
            }
        }
    }
}

// 근무자가 없는 경우 공평한 것으로 간주하여 YES를 출력
if (Object.keys(time_table).length === 0) {
    console.log('YES');
} else {
    // 근무 시간의 최대값과 최소값을 구해서 차이가 12시간 이하인지 확인
    const times = Object.values(time_table);
    const maxValue = Math.max(...times);
    const minValue = Math.min(...times);

    if (maxValue - minValue <= 12) {
        console.log('YES');
    } else {
        console.log('NO');
    }
}