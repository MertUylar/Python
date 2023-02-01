# -*- coding: utf-8 -*-
import pandas as pd

dictionary = {
    "isim":["ali","veli","kenan","ayşe","murat"],
    "yaş":[15,16,17,33,65],
    "maaş":[100,150,200,250,300]    
    
    }

veri= pd.DataFrame(dictionary)
print(veri.head())
print(veri.describe())
print(veri["yaş"])
print(veri.loc[:3,"yaş"])