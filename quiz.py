score=0
quiz=[{"q":"what is the capital of Japan","option":["A.Tokyo","B.okinawa"],"answer":"A"},
      {"q":"what is 12 into 12","option":["A.124","B.144"],"answer":"B"},
      {"q":"which planet is known as evening star","option":["A.mars","B.venus"],"answer":"B"}]
for i in  quiz:
    ques= i["q"]
    option=i["option"]
    correct_ans=i["answer"]
    print(ques)
    for opt in option:
        print(opt)
    ans=str(input("Enter the answer please:"))
    ans=ans.strip().upper()
    if i["answer"]==ans:
        print("correct!","✅")
        score=score+1
    else:
        print("answer is wrong ❌","correct option was",correct_ans)
print(f"your score: {score}/{len(quiz)}")
        
