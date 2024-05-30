import re,sympy
from math import sqrt
from pyscript import document
#import numba 
def seperate_alpha(string):
    _l=re.split("",string)
    l=[]
    for x in _l:
        if x.isalpha():
            l.append(x)
        else:
            pass
    return l

def partial_derivative(formula):
    global _vars
    _vars = seperate_alpha(formula)
    grad=[]
    vars=[]
    for i in range(len(_vars)):
        vars.append(sympy.symbols(_vars[i]))
        #Calculate partial dif
        
        #append into gradient matrix
        grad.append(sympy.diff(formula,vars[i]))
    return grad

#@jit(nopython=True)
def back_substitution(formula,var_value,d):
    global res
    res=[]
    str_grad=[]
    grad=partial_derivative(formula)
    for i in range(len(_vars)):
        str_grad.append(str(grad[i]))
        for j in range(len(_vars)):
            str_grad[i]=str_grad[i].replace(_vars[j],var_value[j])
            
        res.append(eval(str_grad[i]))
    for k in range(len(res)):
        res[k]=float(res[k])
        res[k]=res[k]*float(d[k])
    return res

def split_str(string):
    return re.split(" ",string)
##################################################

def master(event):
    
    #retrieve and organize input data
    _formula=str(document.querySelector("#input").value)
    output=document.querySelector("#output")
    li=seperate_alpha(_formula)
    output.innerText=f"Type in the uncertainty and data in this order:{li}"
    if not(output.innerText==""):
        data=document.querySelector("#data").value
        uncertainty=document.querySelector("#uncertainty").value
        data=split_str(data)
        uncertainty=split_str(uncertainty)
        
        result=back_substitution(_formula,data,uncertainty)
        _result=0
        for i in range(len(result)):
            _result+=result[i]**2
            return sqrt(_result)
        output.innerText=f"Gradient:{partial_derivative(_formula)}\nResult:{_result}"


        

        