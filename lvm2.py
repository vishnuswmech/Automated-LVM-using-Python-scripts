import os


print()
os.system("tput setaf 3")
print("\t\t\tWelcome to Automated LVM")
os.system("tput setaf 7")
print("\t\t\t........................")
os.system("tput setaf 6")
print("""                                               
Press 1: To increase the size
Press 2: To reduce the size
"""
)
os.system("tput setaf 7")
choice=int(input("Enter your choice:"))

if choice==1:
 
 size=int(input("How much actual size you need  (in GB): "))
 os.system("lvextend --size {}G /dev/myvg/mylv".format(size))
 os.system("resize2fs /dev/myvg/mylv")
 
if choice==2:
 reduced_size=int(input("How much actual size you need (in GB): "))
 os.system("umount /dn99")
 os.system("e2fsck -f /dev/mapper/myvg-mylv")
 os.system("resize2fs /dev/mapper/myvg-mylv {}G".format(reduced_size))
 os.system("lvreduce -f --size {}G /dev/mapper/myvg-mylv -y".format(reduced_size))
 os.system("mount /dev/myvg/mylv /dn99")
 
 
 


