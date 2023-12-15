def last_digit_calculator(*args,**kwargs):
    last_digit=[n%10 for n in args]
    value=kwargs.get("op")
    if value=="+":
        print(sum(last_digit))
    elif value=="-":
        result=0
        for n in last_digit:
            result=n-result
        print(result)
    elif value=="*":
        res=1
        for n in last_digit:
            res=n*res
        print(res)

last_digit_calculator(123,24,54,55,34,op="+")
last_digit_calculator(123,24,54,55,34,op="-")
last_digit_calculator(123,24,54,55,34,op="*")
    


        
