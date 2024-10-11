morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
letter = ".... . .-.. .-.. ---"

def solution(letter):
    answer = ''
    sign = letter.split()
    for i in sign:
        answer += morse[i]
    print(answer)
    return answer

solution(letter)