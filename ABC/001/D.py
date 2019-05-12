N = int(input())
SEList = [[int(i) for i in input().split("-")] for _ in range(N)]

# 雨が降った時間が早い順にソート
SEList.sort(key = lambda x : x[0])

# 時間調整
for i, SE in enumerate(SEList):
    SEList[i][0] -= SE[0] % 5
    SEList[i][1] += (5 - SE[1] % 5) if SE[1] % 5 != 0 else 0

# 最終的に答えを入れるリスト
ansList = []
count = 0
ansStart = 10000
ansGoal = -1

while(True):
    # もし記録の最後ならansListに入れる
    if count >= N - 1:
        ansList.append([min(ansStart, SEList[count][0]), max(ansGoal, SEList[count][1])])
        break

    # ansStart: 雨がつながっている記録で最も早いふりはじめの時間
    # ansGoal: 雨がつながっている記録で最も遅く振り終わる時間
    ansStart = min(SEList[count][0], ansStart)
    ansGoal = max(SEList[count][1], ansGoal)

    # つながった雨の振り終わった時間が、次の雨の振りはじめより早かった場合
    # (= 雨がやんだ場合) 降っていた雨の記録をansListに入れ、値を初期化
    if ansGoal < SEList[count + 1][0]:
        ansList.append([ansStart, ansGoal])
        ansStart = 10000
        ansGoal = -1
    # つながった雨の振り終わった時間が、次の雨の振り::じめより遅かった場合
    # (= 雨が続いている場合) ansGoalに最も雨が振り終わるのが遅い時間を入れる
    else:
        ansGoal = max(SEList[count + 1][1], ansGoal)
    count += 1

for ans in ansList:
    print("-".join([str(a).zfill(4) for a in ans]))
