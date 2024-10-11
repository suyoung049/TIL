myString, pat = "ABBAA", 	"AABB"

def solution(myString, pat):
  answer = []
  for str in pat:
    if str == "A":
      answer.append("B")
    elif str == "B":
      answer.append("A")
  change = "".join(answer)
  length = len(change)
  for i in range(0, len(myString) - length + 1):
    if (myString[i:i+length] == change):
      return 1
  
  return 0
 
solution(myString, pat)