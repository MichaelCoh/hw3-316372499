#Michael Cohen 316372499
#A.
def read_line(line_num,file):
    try: text = open(file)
    except:
        return(print("File not found"))
    if type(line_num)!= int:
        return(print("Invalid input detected"))
    lst=[]
    for line in text:
        lst.append(line)
    if len(lst)>=line_num:
        return print(lst[line_num-1])
    else:
        return print("line ",line_num," doesn't exist")
    
#B.
def longest_word(file):
    finallist = []
    try:
        text = open(file)
    except:
        print("File not found")
        return finallist
    fin = open(file)  # Open Text File
    text = fin.read()  # Convert To Big String File
    words = text.split()  # Split into Words
    sorted_list = list(sorted(words, key=len, reverse=True))
    for i in range(5):
        finallist.append(sorted_list[i])
    return finallist  
 