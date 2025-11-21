class Book_keeper:
    bookdata = []

    def __init__(self, bookname, author):    
        if all([bookname, author]):
            self.bookdata.append([bookname , author])
        elif any([bookname, author]):
            print('โปรดกรอกข้อมูลให้ครบถ้วน')
        else:
            print("กรอกรายชื่อหนังสือ และชื่อผู้เขียน เสร็จแล้วพิมพ์ done")
            print("ในรูปแบบ [ชื่อหนังสือ, ชื่อผู้แต่ง]")
            while True:
                usr_input = input().strip().lower()
                if usr_input == 'done':
                    print('สิ้นสุดการทำงาน')
                    break
                __bookname, __author = input().split(',')
                __bookname == __bookname.strip()
                __author == __author.strip()
                self.bookdata.append([__bookname , __author])
    
    def display(self):
        print('หนังสือที่เก็บอยู่มีดังนี้ :')
        for item in self.bookdata:
            print(f'หนังสือ {item[0]} ผู้เขียน {item[1]}')

lib = Book_keeper('How to how to?','pathara muhaha')
lib.display()