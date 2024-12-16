tilecolor = {'white':90,'red':100,'gold':200,'grey':120}

print('------- ราคากระเบื้อง -------')
for c,t in tilecolor.items():
    print(f'สี: {c} ราคา: {t}')

print('------- โปรแกรมคำนวณกระเบื้อง V.2 -------')
try:
    tiles = int(input ('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น : '))
    row = int(input ('1 แถวสามารถปูกระเบื้องได้กี่แผ่น : '))
    color = input('กรุณาเลือกสีกระเบื้อง [white/red/gold] : ')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    tiles = int(input ('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น : '))
    row = int(input ('1 แถวสามารถปูกระเบื้องได้กี่แผ่น : '))
    color = input('กรุณาเลือกสีกระเบื้อง [white/red/gold/grey] : ')
    
print('------- Calculate -------')
total_row = tiles // row
remain_tiles =  tiles % row


buy_more = row - remain_tiles

print(f'มีกระเบื้องทั้งหมด : {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ : {row} แผ่น')
print('------- คำนวณ -------')
print('ต้องปูกระเบื้องทั้งหมด {} แถว'.format(total_row))
print('เหลือกระเบื้องที่ต้องปู {} แผ่น'.format(remain_tiles))
print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม {} แผ่น'.format(buy_more))
print(f'จำนวนเงินที่ต้องซื้อกระเบื้องเพิ่ม {buy_more * tilecolor[color]} บาท')

print('---------- The End -----------')
