# library = [...[id,name,author,cateogory,arrival[borrower,cdate,rdate,fine],rating]...]
# Default = 50 | Fine = 5 Per Day
# New : Added Ratings

library=[]

from datetime import date as datetime
from datetime import timedelta

today = datetime.today()

def sortByDate(lib):
    n = len(lib)
    for i in range(n):
      for j in range(0, n-i-1):
        if lib[j][5][2] > lib[j+1][5][2] :
          lib[j], lib[j+1] = lib[j+1], lib[j]
              
def sortByRatings(lib):
  n = len(lib)
  for i in range(n):
    for j in range(0, n-i-1):
      a1,a2=lib[j][6],lib[j+1][6]
      a1,a2=sum(a1)/len(a1),sum(a2)/len(a2)
      if a1 > a2 :
        lib[j], lib[j+1] = lib[j+1], lib[j]
              
#ToDo: Fix display (Done @ 80%)
def display(set,flag): # helps to portrait the results
  #book=[id,name,author,cateogory,arrival[borrower,cdate,rdate,fine]]
  if flag == False:
    print("id\tname\tauthor\tcateogory\tarrival\tRatings")
    i = 0
    for book in set:
      semic=book[-1]
      semic=sum(semic)/len(semic)
      for det in book:
        print(det,end="\t")
        i+=1
        if i==6:
          break
        print(semic)
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
  for bk in library:
    if bk[0]==id:
      print("Sorry, but the id is already entered")
      id=(input("Enter New id:"))
  adate=today
  ratings=[] # fix rating system
  book=[id,name,auth,cat,adate,[False,False,False,False],ratings]
  library.append(book)
  print("Added",str(len(library))+"th book",library[-1][1])
  #print(library)

def search(filter,type):
  req=[]#to be sold
  req_s=[] #already sold
  for book in library:
    if book[type]==filter:
      if book[5][0] is False:
        req.append(book)
      else:
        req_s.append(book)
  sortByDate(req_s)
  sam = [req,req_s] # 0 unsold ; 1 sold
  return sam

def p_search():
  print("Select by which you want to filter \n1 for id\n2 for name\n3 for author \n4for cateogory")
  t1 = int(input("Enter the field:"))-1
  f1 = input("Enter search: ")
  r=search(f1,t1)
  display(r[0],False) # ToDo: Fix display
  print();print("Books upto come: ")
  display(r[1],True)
  
def change_com(id_r,flag,stat): # stat: 0 unsold ; 1 sold
  room = search(id_r,0)
  room = room[stat]
  for books in room:
    book_r = books
  if flag == 1:
    book_r[5][0]=input("Borrower Name:")
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
    #print(today,date)
    if type(date) is not bool:
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
  m=search(id_pay,0)
  for i in m:
    pass
  for j in i:
    print(j)
  date = j[5][2]
  #print(fine)
  fine = today-date
  fine=fine.days*5
  j[5][3]=fine
  change_com(id_pay,fine,1)
  rater=int(input("How much would you rate this book for 5:"))
  while True:
    if rater<=5:
      print("Thank you for Feedback")
      break
    else:
      print("Sorry, Enter value than 5")
      rater=int(input("How much would you rate this book for 5"))
    rate_fi=m[6]
    rate_fi.append()
  print("Thank you for borrowing books from us. Hope you visit us next time.")

#--------------------------------------------------------------------------------------------------------
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
    change_com(me,1,0)
  elif op == 4:
    check(True)
  elif op == 5:
    mep = input("Enter id:")
    checkout(mep)
  elif op == 6:
    break
  """
  Caution:
  Code 198 is made for Develepors for testing the Software
  and demo Please disable this feature for production
  """
  # elif op == 198:
  #   print("Warning: Entering into Developer Mode.\n This is to change current date\n This is made only for Testing.")
  #   p = []
  #   qus = ("Year","Month","Day")
  #   for q in qus:
  #     query = ""
  #     defi = "Enter New",q,":"
  #     for de in defi:
  #       query+=de+" "
  #     epo = int(input(query))
  #     p.append(epo)
  #   # Creating Future today
  #   today = datetime(p[0],p[1],p[2])
  #   print("Entering Future. Assume that day is",today)
  # print("------------------------------------")
