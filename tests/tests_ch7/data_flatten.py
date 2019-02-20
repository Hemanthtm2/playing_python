#!/usr/bin/python

nested= {
   'fullname':'Alessandra',
   'age':41,
   'phone-numbers':['+447421234567','+447423456789'],
   'residence': {
         'address': {
               'first-line':'Alexandra Rd',
               'second-line': '',
                    },
                    'zip': 'N8 0PP',
                    'city': 'London',
                    'country': 'UK',
                   },
               }

flat={
   'fullname':'Alessandra',
   'age':41,
   'phone-numbers':['+447421234567','+447423456789'],
   'residence.address.first-line':'Alexandra Rd',
   'residence.address.second-line':'',
   'residence.zip':'N8 0PP',
   'residence.city':'London',
   'residence.country':'UK',
   }


def flatten(data,prefix='',seperator='.'):

    if not isinstance(data,dict):
       return {prefix:data} if prefix else data 
    result={}

    for (key,value) in data.items():
         result.update(flatten(value,_get_new_prefix(prefix,key,seperator),seperator=seperator))

    return result


def _get_new_prefix(prefix,key,seperator):
    return (seperator.join((prefix,str(key)))
           if prefix else str(key))
