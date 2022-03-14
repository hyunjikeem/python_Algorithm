def solution(board, moves):
    bucket = []
    answer = 0
    
    for move in moves :
        for line in board :
            if line[move-1] != 0 :
                bucket.append(line[move-1])
                line[move-1] = 0
                # break
                
                if len(bucket) > 1 :
                    if bucket[-1] == bucket[-2] :
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer += 2
                break
    
    return answer