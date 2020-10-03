class Kingdom:
    
    # Contains Attributes of class Kingdom 
    def __init__(self, kingdom, emblem):
        
        self.kingdom = kingdom
        self.emblem = emblem
        self.shift = len(self.emblem)        
        
    # Method to decrypt the secret message in the input file.
    def decrypt(self): 
        
        result = "" 
        self.shift = 26-self.shift
        # traverse text 
        for i in range(len(self.text)): 
            char = self.text[i] 
    
            # decrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + self.shift-65) % 26 + 65) 
    
            # decrypt lowercase characters 
            else: 
                result += chr((ord(char) + self.shift - 97) % 26 + 97) 
        return(result) 
    
    # Method to check for a given kingdom, if the secret message consists of EMBLEM (characters) in it or not.
    def check_kingdom(self,text):
        
        self.text = text
        self.text = (self.text).replace(self.emblem,"")
        
        text_char_list = list(self.decrypt())
        emblem_char_list = list(self.emblem)
        
        #Checks for a character match from Emblem name with decrypted text. If match found, the element is popped from emblem_char_list.
        if len(text_char_list)>len(emblem_char_list):
            for k in text_char_list:
                for j in emblem_char_list:
                    if k==j:
                        emblem_char_list.pop(emblem_char_list.index(j))
                    
        else:
            for k in emblem_char_list:
                for j in text_char_list:
                    if k==j:
                        emblem_char_list.pop(emblem_char_list.index(k))
                        
        #If all the characters from emblem name are matched and popped in the decrypted text and the list is empty, then return Kingdom as ally.
        if len(emblem_char_list) == 0:
            return(self.kingdom)

import sys

#Reads Kingom and Secret Message from input file and passes it to class methods and stores its allies.
def main():

    ruler='SPACE '
    min_allies = 3 
    
    #Stores the Keyvalue pair for Kingdom and Emblem.
    kingdom_emblem_dic = {'SPACE':'GORILLA', 'LAND':'PANDA', 'WATER':'OCTOPUS', 'ICE':'MAMMOTH', 'AIR':'OWL', 'FIRE':'DRAGON' }
    allies=[]
    
    #Read Input from the input file and stores in variable lines.
    with open(" ".join(sys.argv[1:]), 'r') as f:
        lines=f.readlines()
    
    #Iterates over each line.
    for i in lines:
        input_list = i.split(' ')
        kingdom_input = input_list[0]            #First word of the input file is the Kingdom.
        text_input = " ".join(input_list[1:])    #Rest of the line contains a secret text message.
        
        #In each line , We collects the kingdom and corresponding emblem value. And create a class object passing kingdom,emblem,secret message.
        for i in kingdom_emblem_dic.keys():
            if kingdom_input == i: 
                kingdom_obj = Kingdom(i,kingdom_emblem_dic[i])
                allies.append(kingdom_obj.check_kingdom(text_input)) #Store the allies in a list by calling check_kingdom method.
    
    result = list(filter(lambda x: x != None, allies)) #Filters only allies removing Null values from the list.
    result = list(dict.fromkeys(result)) #Remove duplicate allies
    
    #Checks if atleast 3 allies are present or not.
    
    if len(result) >= min_allies: 
        print(ruler + " ".join(result)) #Prints output line with allies
    else:
        print("None")   #prints none if it has not got enough allies.
    

if __name__ == "__main__":
    main()