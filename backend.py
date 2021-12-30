# library = [...[id,name,author,cateogory,arrival[borrower,cdate,rdate,fine]]...]
# Default = 50 | Fine = 5 Per Day

library=[]

from datetime import datetime,timedelta

today = datetime.now()


def display(set,flag): # helps to portrait the results
  #book=[id,name,author,cateogory,arrival[borrower,cdate,rdate,fine]]
  if flag == False:
    print("id\tname\tauthor\tcateogory\tarrival")
    for book in set:
      for det in book:
        print(det,end="\t")
      print()
  elif flag == True:
    print("id\tname\tauthor\tcateogory\tarrival\tborrow\tDate\tReturn\tFine")
    for book in set:
      for det in book:
        if type(det)==list:
          for i in det:
            print(i,end="\t")
        else:
          print(det,end="\t")
      print()

def entry(): # Automated Entry System
  name = input("Enter book name:")
  auth = input("Author Name:")
  cat=input("Enter which caateogory:")
  id=(input("Enter New id:"))
  adate=today
  book=[id,name,auth,cat,adate,[False,False,False,False]]
  library.append(book)
  print("Added",str(len(library))+"th book",library[-1][1])
  #print(library)

def search(filter,type):
  req=[]
  req_r=[]
  for book in library:
    if book[type]==filter:
      if book[5][0] is not False:
        req.append(book)
      else:
        req_r.append(book)
  sam = [req,req_r]
  return sam

def p_search():
  print("Select by which you want to filter \n1 for id\n2 for name\n3 for author \n4for cateogory")
  t1 = int(input("Enter the field:"))-1
  f1 = input("Enter search: ")
  r=search(f1,t1)
  display(r[1],True)
  
def change_com(id_r,flag): # flag => 1(new)
  room = search(id_r,0)
  room = room[1]
  for books in room:
    book_r = books
  if flag == 1:
    book_r[5][0]=input("Borrower Name")
    book_r[5][1]=today
    delt = timedelta(days=15)
    book_r[5][2]=today+delt
    print("{} has borrowed {} should return at {}".format(book_r[5][0],book_r[1],book_r[5][2]))
  else:
    det = book_r[5]
    print("{} has returned {} at {} and payed{}".format(book_r[5][0],book_r[1],today,flag))
    for x in det:
      x=False 

def check(flag):
  fault = []
  for m in library:
    date = m[5][2]
    print(today,date)
    if date>today:
      fine = m[5][3]
      fine = today-date
      fine=int(fine.days)*5
      fault.append(m)
  if flag == True:
    for wr in fault:
      print(wr[1],"borrowed by",wr[5][0],"and has to pay",str(50+fine))

def checkout(id_pay):
  check(False) # Update Fine
  fine = m[5][3]
  fine = today-date
  fine=fine.days*5
  change_com(id_pay,fine)
  print("Thank you for borrowing books from us. Hope you visit us next time.")
menu="1 for Entering Books \n2 for search \n3 for cashier system \n4 for Checking Fine \n5 for Bill display \n6 for end"
while True:
  print(menu)
  op = int(input("Enter choice"))
  if op == 1:
    entry()
  elif op == 2:
    p_search()
  elif op == 3:
    me = input("Enter id:")
    change_com(me,1)
  elif op == 4:
    check(True)
  elif op == 5:
    mep = input("Enter id:")
    change_com(mep)
  elif op == 6:
    break
  print("------------------------------------")
