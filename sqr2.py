n=int(input("Enter the number of elements:"))
num_list=[]
for i in range(n):
 a=int(input("Enter the numbers:"))
 num_list.append(a)
print("Entered list:",num_list)
sqr_lst=[x**2 for x in num_list]
print("Squared list:",sqr_lst)