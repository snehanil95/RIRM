import re 

def main():
	fd=open ("phonenum.txt",'r')
	num=fd.readline()

	for num in fd:
	    print(num)
	    r=re.fullmatch('^\+?(44)?(0|7)\d{9,13}$',num)
	    print(r)
	    if r==None: 
		    print('Valid Number')
	    else:
		    print('Not a valid number')

if __name__ == "__main__":
    main()