#!/usr/bin/env python

#Imports
import urllib
import json
import isbnlib
from pprint import pprint



def get_book_info(isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn
    print url
    response = urllib.urlopen(url)
    book = json.loads(response.read())
    book_dic = {}
    if book['totalItems'] == 0:
        print ('There seems to be an error with the isbn, no book could be found')
        book = isbnlib.meta(isbn)
        if book == None:
            print('Giving up, try and look for it on amazon')
        else:
            book_dic['authors'] = book['Authors'][0]
            book_dic['title'] = book['Title']
            book_dic['year'] = book ['Year']
            book_dic['language'] = book ['Language']
            book_dic['pageCount'] = 'u'
            book_dic['subtitle'] = 'u'
            
    else:
        book_dic['authors'] = book['items'][0]['volumeInfo']['authors'][0]
        book_dic['language'] = book['items'][0]['volumeInfo']['language']
        book_dic['pageCount'] = book['items'][0]['volumeInfo']['pageCount']
        book_dic['title'] = book['items'][0]['volumeInfo']['title']
        book_dic['subtitle'] = book['items'][0]['volumeInfo']['subtitle']
        book_dic['year'] = book['items'][0]['volumeInfo']['publishedDate']
    return book_dic

if __name__ == '__main__':
    

    f = open('data/data.txt', 'r')
    data = f.readlines()
    f.close()

    dictionary_list = []
    for l in data:
        entry =  l.split(' ')
        e = entry[0]
        ISBN=e.split('：')
        if ISBN[0]!='ISBN':
            print 'wrong format of file, first entry should be an ISBN!'
        print (ISBN[1])
        #get_book_info(ISBN[1])
        dictionary_list.append(get_book_info(ISBN[1]))
        print ('===============================')