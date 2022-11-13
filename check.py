file1=open(r"C:\Users\ds\Desktop\file1.txt")
text1=file1.readlines()
text1


file2=open(r"C:\Users\ds\Desktop\file2.txt")
text2=file2.readlines()
text2



# Convert list to string 

str1=''.join(text1)
str2=''.join(text2)


# Split the string

sent_text1=str1.split('.')
sent_text2=str2.split('.')


# Create a for loop that compares two lists

final_list=[]
for z in sent_text1:
    for y in sent_text2:
        if z == y:
            final_list.append(z)



print(final_list)