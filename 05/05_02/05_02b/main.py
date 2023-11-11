from collections import deque

printer_queue = deque()
printer_queue.append("ticket.png")
printer_queue.append("list-of-ppl.docx")
printer_queue.append("install_guide.pdf")

while len(printer_queue) > 0:
    document = printer_queue.popleft()
    print(f"Printing {document} ...")
