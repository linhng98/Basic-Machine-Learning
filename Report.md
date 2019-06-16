# Đồ  Án Logic Mệnh Đề

Họ tên          | Mã số sinh viên | Đóng góp                                                            | Hoàn Thành
--              |              -- | --                                                                  | --
Đoàn Khuê       |         1612311 | đồ án 1 output, đồ án 2 logic và input output, viết báo cáo đồ án 2 | 70%
Nguyễn Văn Linh |         1612340 | đồ án 1 logic, đồ án 2 input output, viết báo cáo đồ án 1           | 100%

---
## Mục lục

- [Đồ Án Logic Mệnh Đề]()
  - [Mục lục]()
  - [Đồ án 1]()
    - [Giải Thuật]()
    - [Ý nghĩa các hàm]()
    - [Cách sử dụng]()
    - [Kết quả đạt được]()
  - [Đồ án 2]()
    - [Giải Thuật]()
    - [Ý nghĩa các hàm]()
    - [Cách sử dụng]()
    - [Kết quả đạt được]()
  - [Tham Khảo]()

---

## Đồ án 1

### Giải Thuật

![algorithm flow chark](resources/logic_and_predicate/algorithm_flowchart.png)

### Ý nghĩa các hàm

```python
def check_clause_B_is_sub_clause_A_AND(clause_A, clause_B):
```
* Kiểm tra xem mệnh đề B (có dạng X.Y) có nằm trong mệnh đề A hay không
* Return boolen 

```python
def check_clause_B_is_sub_clause_A_OR(clause_A, clause_B):
```
* Kiểm tra xem mệnh đề B (có dạng X+Y) có nằm trong mệnh đề A hay không
* Return boolen 

```python
def check_clause_B_is_EQ_clause_A(clause_A, clause_B):
```
* Kiểm tra mệnh đề B có suy ra được mệnh đề A không
* Return boolen

```python
def nCr(n, r):
```
* Tính số lượng các cặp mệnh đề khác nhau trong danh sách
* Return số lượng các cặp mệnh đề 

```python
def negative_clause(clause):
```
* Phủ định mệnh đề
* Return mệnh đề đã được phủ định

```python
def check_valid_syntax(clause):
```
* Kiểm tra cú pháp mệnh đề có hợp lệ hay không
* Return boolen

```python
def remove_double_negative(clause):
```
*  Áp dụng luật EQ rút gọn mệnh đề có dạng phủ định của phủ định
*  Return mệnh đề đã được rút gọn

```python
def check_is_equal(clause_A, clause_B):
```
* Kiểm tra mệnh đề A có tương đương với mệnh đề B không
* Return boolen

```python
def check_is_negative(clause_A, clause_B):
```
* Kiểm tra mệnh đề A có phải là dạng phủ định của mệnh đề B không
* Return boolen

```python
def append_deduction_list(clause, proof):
```
* Thêm mệnh đề vào danh sách, cùng với dẫn chứng đã sử dụng để suy ra mệnh đề đó
* Return 

```python
def input_amount_premise():
```
* Nhập số lượng tiền đề
* Return

```python
def input_list_premise(amount_premise):
```
* Nhập các tiền đề
* Return

```python
def input_conclude():
```
* Nhập kết luận
* Return

```python
def implement_CON_rule(clause_A, clause_B, idx_A, idx_B):
```
* Áp dụng Conjunction rule cho mệnh đề  A và B 
* Return

```python
def check_HS_rule(clause_A, clause_B, idx_A, idx_B):
```
* Kiểm tra Hypothetical Syllogism rule giữa 2 mệnh đề A B, nếu tồn tại quan hệ thì áp dụng Hypothetical Syllogism rule
* Return 

```python
def natural_deduction(clause_A, clause_B, idx_A, idx_B):
```
* Hàm thực thi các luật Modus Ponens, Modus Tollens, Simplification, Addition
* Return

```python
def check_all_pair():
```
* Hàm thực hiện vòng lặp duyệt toàn bộ mệnh đề có trong danh sách
* Return

```python
def main():
```
* Hàm main của chương trình
* Return


### Cách sử dụng

* Cài đặt python
* Chạy chương trình bằng câu lệnh `python natural_deduction_logic.py`
* Nhập số lượng tiền đề
* Nhập tiền đề
* Nhập kết luận
* Chỉ sử dụng các chữ cái in hoa và các kí tự `(`, `)`, `-`, `.`, `+`, `>`, `=`

### Kết quả đạt được

![](resources/logic_and_predicate/demo_result_1.png)
![](resources/logic_and_predicate/demo_result_2.png)
![](resources/logic_and_predicate/demo_result_3.png)

## Đồ án 2

### Giải Thuật
### Ý nghĩa các hàm chính
### Cách sử dụng

Tạo một file `input.txt` với nội dung là các mệnh đề và dòng cuối cùng là kết luận

Ví dụ:

```
E . F > D
A + -B + -D
-A
F . E
-B
```

Sau đó chạy chương trình bằng lệnh `python project2.py`

### Kết quả đạt được

Chức năng | Hoàn thành
:--       |        --:
Đọc được input từ file          | 100%
Biến đổi các câu thành dạng CNF | 100%
Lấy phủ định kết luận           | 100%
Kiểm tra mệnh đề mâu thuẫn      |  10%
Hợp giải                        |   0%

### Tham Khảo

* [https://en.wikipedia.org/wiki/Natural_deduction](https://en.wikipedia.org/wiki/Natural_deduction)
* [https://www.iep.utm.edu/nat-ded/](https://www.iep.utm.edu/nat-ded/)
* [https://proofs.openlogicproject.org/](https://proofs.openlogicproject.org/)
* [https://github.com/ldkrsi/cnf_py](https://github.com/ldkrsi/cnf_py)
* [https://github.com/khamkarajinkya/Davis-Putnam-Logemann-Loveland-Algorithm](https://github.com/khamkarajinkya/Davis-Putnam-Logemann-Loveland-Algorithm)