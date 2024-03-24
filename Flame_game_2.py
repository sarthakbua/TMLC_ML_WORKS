# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:48:34 2024

@author: Sarthak
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:22:01 2024

@author: Sarthak
"""





def flame_funtion(name1 , name2):
    
    flames="flames"
    
    for letter in name1:
        if letter in name2:
            name2=name2.replace(letter,"",1)
            name1=name1.replace(letter,"",1)
    
    flamed_name = name1 + name2
    print(flamed_name)
    letter_count=len(flamed_name)


    while len(flames) > 1:
        letter_index= ( letter_count%len(flames) ) - 1
        
        if  letter_index >= 0:
            # list comprehension
            right=flames[letter_index + 1:]
            left=flames[:letter_index]
            flames=right + left
            
        else:
            flames=flames[:len(flames) - 1]
              
 
     
    return flames         

def relation_interpretation(result):

    out = {
        'f': 'Friendship',
        'l': 'Love',
        'a': 'Affection',
        'm': 'Marriage',
        'e': 'Enemy',
        's': 'Siblings'
    }
    return out[result]
    
def main():
    
    print("FLAME Game")
    print ("● Friends")
    print ("● Lovers")
    print ("● Affectionate")
    print ("● Marriage")
    print ("● Enemies")
    print ("● Siblings")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    name1 = name1.replace(" ","").lower()
    name2 = name2.replace(" ","").lower()
    

    
    print( name1 +" "+ name2)
    res = flame_funtion(name1,name2)
    relation = relation_interpretation(res)
    
    print( "Relationship between " +name1 +" & "+name2 +" "+ relation )
    
if __name__ == "__main__":
   main()     