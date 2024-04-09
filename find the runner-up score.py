if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr, reverse=True)
    maximum_num = max(arr)
    
    runner_up_score = None
    for score in sorted_arr:
        if score < maximum_num:
            runner_up_score = score
            break
    
    print(runner_up_score)
