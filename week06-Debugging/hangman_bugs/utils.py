"""
You can ignore this file, some of the functions are a little more advanced and will not include any bugs for you to find (unless I messed up...)
"""

import random,os
import pandas as pd

def title():
    return """
$$\   $$\                                                                 
$$ |  $$ |                                                                
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  
$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ 
$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |
\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|
                              $$\   $$ |                                  
                              \$$$$$$  |                                  
                               \______/                                   
"""

def get_random_sentence():
    sentences = pd.read_csv(os.path.abspath('./sentence_list.csv'))
    
    idx = random.randint(0, len(sentences.index) - 1)

    return sentences.loc[idx,"Sentence"].upper(), sentences.loc[idx,"Category"] 