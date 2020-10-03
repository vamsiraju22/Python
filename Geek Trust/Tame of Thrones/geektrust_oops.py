class Kingdom:
    
    # Contains Attributes of class Kingdom 
    def __init__(self, kingdom, emblem,text):
        
        self.kingdom = kingdom
        self.emblem = emblem
        self.shift = len(self.emblem)
        self.text = text
    
    # Method to decrypt the secret message in the input file.
    def decrypt(self): 
        
        result = "" 
        self.shift = 26-self.shift
        # traverse text 
        for i in range(len(self.text)): 
            char = self.text[i] 
    
            # decrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + shift-65) % 26 + 65) 
    
            # decrypt lowercase characters 
            else: 
                result += chr((ord(char) + shift - 97) % 26 + 97) 
        return(result) 
    
    # Method to check for a given kingdom, if the secret message consists of EMBLEM (characters) in it or not.
    def check_kingdom(self):
        
        res = decrypt(self.text,self.shift)
        unique_res = list(set(res))
        unique_kingdom = list(set(self.emblem))
        
        for k_ind,k in enumerate(unique_res):
            for j_ind,j in enumerate(unique_kingdom):
                if k == j:
                    unique_kingdom.pop(j_ind)
        
        if len(unique_kingdom) == 0:
            return(self.kingdom)

import sys

#Reads Kingom and Secret Message from input file and passes it to class methods.
def main():

    ruler='SPACE '
    with open(" ".join(sys.argv[1:]), 'r') as f:
        lines=f.readlines()
    
    #Stores the Keyvalue pair for Kingdom and Emblem.
    kingdom_emblem_dic = {'SPACE':'GORILLA', 'LAND':'PANDA', 'WATER':'OCTOPUS', 'ICE':'MAMMOTH', 'AIR':'OWL', 'FIRE':'DRAGON' }
    allies=[]
    
    for i in lines:
        input1_list = i.split(' ')
        kingdom_input = input1_list[0]
        text_input = input1_list[1]
        
        for i in kingdom_emblem_dic.keys():
            if kingdom_input == i:
                kingdom_obj = Kingdom(i,kingdom_emblem_dic[i],text_input)
                allies.append(kingdom_obj.check_kingdom())
    
    result = list(filter(lambda x: x != None, allies))
    
    if len(result) >= 3:
        print(ruler + " ".join(result))
    else:
        print("None")   
    

if __name__ == "__main__":
    main()