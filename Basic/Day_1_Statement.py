# Single Line
a = 10

# Multiple line ( \ -> used for next line )
a = 12; b =12

c = a + b\
    +10

print(c)
print() 


var1,var2,var3 = 10,20,30

print(var1,var2,var3)
print()

var1=var2=var3 = 10
print(var1,var2,var3)
print()

#Numeric Literal
bin = 0b1011
oct = 0o12
hex = 0xA

print(bin,oct,hex)
print()


#float Literal
var1 = 12.12
var2 = 12.1e5  # e = 10^x
print(var1)
print(var2)
print()

#complex Literal
cmp = 3+4j
print(cmp)
print(cmp.real)
print(cmp.imag)



#Special literal

a= None  # NULL = absence of value
print(a)



# Know Type

a = 10
print(type(a))

a= 10.20
print(type(a))

b = "String B"
print(isinstance(b, str))
