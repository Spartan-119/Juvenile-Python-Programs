def solution(l):
    # Your code here
    x = []
    for i in l:
        x.append(i.split("."))
    #return x
    
    # the res list contains the splitted elements as "Strings"
    # we need to change them into int
    
    # to do that we will use map method of lists
    result = []
    for i in x:
        result.append(list(map(int, i)))
    for i,version in enumerate(result):
        list(result[i])
    
    
    # now we will return the final answer separated by period "."
    sorted_result = sorted(result)
    
    
    
    #res = [item.replace('.', ',') for item in sorted_result]
    
    #print(sorted_result)
    final_result = [".".join(str(j) for j in i) for i in sorted_result]
    
    return final_result


t = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
print(solution(t))
    
    