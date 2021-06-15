from BackEnd.Borrow import borrow
from BackEnd.attendace import attempt,getStudentData
from BackEnd.ReturnBook.returnBook import getBorrowData

print("Enter your name:")
print("1. pinjam buku")
print("2. kembalikan buku")
print("3. absen")
x = int(input())

if x == 1:
    student = getStudentData()
    if (student != 0):
        borrow(student)
elif x == 2:
    student = getStudentData()
    if(student != 0):
        getBorrowData(student)
elif x == 3:
    id = str(input("rfid: "))
    rfid = {'rfid' : id}
    attempt(rfid)


