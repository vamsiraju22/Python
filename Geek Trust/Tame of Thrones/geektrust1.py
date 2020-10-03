
import sys

def decrypt(text,shift): 
    result = "" 
    shift = 26-shift
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 

        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + shift-65) % 26 + 65) 

        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + shift - 97) % 26 + 97) 
    return(result) 


def get_res(kingdom,text):

    kingdom_emblem_dic = {'SPACE':'GORILLA', 'LAND':'PANDA', 'WATER':'OCTOPUS', 'ICE':'MAMMOTH', 'AIR':'OWL', 'FIRE':'DRAGON' }
    emblem_len_list = [len(kingdom_emblem_dic[i]) for i in kingdom_emblem_dic.keys()]
    kingdom_list = [i for i in kingdom_emblem_dic.keys()]
    kingdom_emblem_len_dic = dict(zip(kingdom_list,emblem_len_list))
    
    for i in kingdom_emblem_len_dic.keys():
        if i == kingdom:
            res = decrypt(text,kingdom_emblem_len_dic[i])
            unique_res = list(set(res))
            unique_kingdom=list(set(kingdom_emblem_dic[i]))
            
            for k_ind,k in enumerate(unique_res):
                for j_ind,j in enumerate(unique_kingdom):
                    if k==j:
                        unique_kingdom.pop(j_ind)
            if len(unique_kingdom)==0:
                return(kingdom)
            
                

def main():

    ruler='SPACE '
    with open(" ".join(sys.argv[1:]), 'r') as f:
        lines=f.readlines()
    
    output=[]
    for i in lines:
        input1_list=i.split(' ')
        kingdom=input1_list[0]
        text=input1_list[1]
        output.append(get_res(kingdom,text))
    
    result = list(filter(lambda x: x != None, output))
    if len(result)>=3:
        output_file=ruler+" ".join(result)
        print(output_file)
    else:
        output_file="None"
        print(output_file)   
    

if __name__ == "__main__":
    main()