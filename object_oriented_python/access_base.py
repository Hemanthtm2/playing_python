#!/usr/bin/python



class Book():
    def __init__(self,title,publication,price):
                 self.title=title
                 self.publication=publication
                 self.price=price


class EBook(Book):
    def __init__(self,title,publication,price,format_):
                Book.__init__(self,title,publication,price)
                self.format_=format_
          

ebook=EBook('Learning Python','Packt',360,'PDF')

print(ebook.title)

print(ebook.publication)

print(ebook.price)

print(ebook.format_)
