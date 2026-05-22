# Câu 1:
price = int(input("Nhập vào Đơn giá của một sản phẩm: "))
quantity = int(input("Nhập vào Số lượng mua: "))

total_price = price * quantity

if total_price >= 1000000:
    total_price = total_price * 0.9

print("Số tiền cuối cùng khách hàng phải thanh toán là: ", total_price)



# Câu 2:
password = "123456"
count = 0
is_valid = True

while count != 3:
    input_web = input("Nhập Password để đăng nhập: ")
    if input_web == password:
        print("Đăng nhập thành công!")
        break
    else:
        count += 1
        is_valid = False
        print(f"Mật khẩu sai lần {count}, Vui lòng nhập lại!")

if is_valid == False:
    print("Đã nhập quá 3 lần. Tài khoản của bạn đã bị khóa!");



# Câu 3:
total_products = 0
index = 1
count_box = 0

while True:
    numbers_product = int(input(f"Nhập vào số lượng sản phẩm thùng {index}: "))
    index += 1
    if numbers_product < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        continue

    if numbers_product == 0:
        break
    
    if numbers_product > 0:
        count_box += 1
        total_products += numbers_product

print("\n--------------------------------------------")
print(f"Tổng số thùng hàng hợp lệ đã đếm: {count_box} thùng hàng hợp lệ")
print(f"Tổng số sản phẩm thu được: {total_products} sản phẩm")