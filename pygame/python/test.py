class Node:
    """คลาสสำหรับสร้าง Node แต่ละตัว"""
    def __init__(self, data):
        self.data = data      # เก็บข้อมูล
        self.next = None      # ตัวชี้ไปยัง Node ถัดไป (เริ่มต้นเป็น None)

class LinkedList:
    """คลาสจัดการ Linked List"""
    def __init__(self):
        self.head = None      # จุดเริ่มต้นของ List

    # ---------------------------------------------------
    # ส่วนที่ 1: การเพิ่มข้อมูล (Insertion)
    # ---------------------------------------------------

    def insert_at_begin(self, data):
        """เพิ่ม Node ใหม่ที่ด้านหน้าสุด (InsertAtBegin)"""
        new_node = Node(data)
        new_node.next = self.head  # ชี้ next ของ node ใหม่ไปที่ head เดิม
        self.head = new_node       # ย้าย head มาที่ node ใหม่

    def insert_at_end(self, data):
        """เพิ่ม Node ใหม่ที่ด้านหลังสุด (InsertAtEnd)"""
        new_node = Node(data)

        # ถ้า List ว่างอยู่ ให้ตัวใหม่เป็น Head เลย
        if self.head is None:
            self.head = new_node
            return

        # ถ้าไม่ว่าง ให้วิ่งหาตัวสุดท้าย
        last = self.head
        while last.next:           # วนลูปจนกว่าจะเจอตัวที่ next เป็น None
            last = last.next

        last.next = new_node       # ต่อท้ายด้วย node ใหม่

    def insert_at_index(self, index, data):
        """เพิ่ม Node ใหม่ที่ตำแหน่งที่ระบุ (InsertAtIndex)"""
        if index == 0:
            self.insert_at_begin(data)
            return

        new_node = Node(data)
        current = self.head

        # วิ่งไปหาตำแหน่งก่อนหน้า index ที่ต้องการ (index - 1)
        for _ in range(index - 1):
            if current is None:
                print("Index out of range")
                return
            current = current.next

        if current is None:
             print("Index out of range")
        else:
            new_node.next = current.next
            current.next = new_node

    # ---------------------------------------------------
    # ส่วนที่ 2: การลบข้อมูล (Deletion)
    # ---------------------------------------------------

    def remove_first_node(self):
        """ลบ Node แรกสุด (RemoveFirstNode)"""
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next  # ย้าย Head ไปตัวถัดไป (ตัวแรกจะหายไปเอง)

    def remove_last_node(self):
        """ลบ Node สุดท้าย (RemoveLastNode)"""
        if self.head is None:
            print("List is empty")
            return

        # กรณีมีแค่ Node เดียว
        if self.head.next is None:
            self.head = None
            return

        # กรณีมีหลาย Node วิ่งหาตัวรองสุดท้าย
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next

        second_last.next = None     # ตัดหางทิ้ง

    def remove_at_index(self, index):
        """ลบ Node ที่ตำแหน่งที่ระบุ (RemoveAtIndex)"""
        if self.head is None:
            print("List is empty")
            return

        if index == 0:
            self.remove_first_node()
            return

        current = self.head
        # วิ่งหาตัวก่อนหน้าที่จะลบ
        for _ in range(index - 1):
            if current.next is None:
                print("Index out of range")
                return
            current = current.next

        # ทำการข้าม Node ที่ต้องการลบ (Link ข้ามหัวไปเลย)
        if current.next is None:
             print("Index out of range")
        else:
             current.next = current.next.next

    # ---------------------------------------------------
    # ฟังก์ชันแสดงผล (Utility)
    # ---------------------------------------------------
    def print_list(self):
        """แสดงข้อมูลทั้งหมดใน Linked List"""
        temp = self.head
        if not temp:
            print("List is empty")
            return

        while temp:
            print(f"[{temp.data}] -> ", end="")
            temp = temp.next
        print("None")

# ==========================================
# ส่วนทดสอบการทำงาน (Driver Code)
# ==========================================
if __name__ == "__main__":
    llist = LinkedList()

    print("1. สร้างและเพิ่มข้อมูล:")
    llist.insert_at_begin(10)  # List: 10
    llist.insert_at_begin(5)   # List: 5 -> 10
    llist.insert_at_end(20)    # List: 5 -> 10 -> 20
    llist.insert_at_index(2, 15) # แทรก 15 ที่ index 2 -> List: 5 -> 10 -> 15 -> 20
    llist.print_list()

    print("\n2. ลบข้อมูล:")
    print("ลบตัวแรก (5):")
    llist.remove_first_node()
    llist.print_list()

    print("ลบตัวสุดท้าย (20):")
    llist.remove_last_node()
    llist.print_list()

    print("ลบที่ Index 1 (คือเลข 15):")
    llist.remove_at_index(1)
    llist.print_list()