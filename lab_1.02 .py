'''
Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2                  9                                           No
b   2/3                        0.6666666666666                              
c   2.0 * 1.5                  3.0                                         It kept the .0 
d   (2 + 3) * 10                50                                           
e   5.0 // 2                    2    
f   5.0 % 2                     1.0

Section 2
    Input                   Output                          Did it do something unexpected?
a   a              NameError: name 'a' is not defined                   Gave an error
b   'a'                        'a'                                            

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'                     'a+b'
b   'a' + 'b'                 'ab'                              put the ab inside the '' instead of leaving them separated  

Section 4
    Input                   Output                                                  Did it do something unexpected?
a   'a' * 'b'    TypeError: can't multiply sequence by non-int of type 'str'            gave an error for multiplying non integer type of string
b   'a' * 2                     'aa'

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                           20
b   .5 * 2                      integer                   1                                           1.0; should be float
c   10/2                        integer                    5                                        5.0; should be float      
d   10%2                        integer                0                                             0      
e   2 ** 3                      integer               8                                                 8  
f   (2+5)*3                         integer                 21                                           21   
g   2 + 5 * 3                           integer              17                                           17  
h   'ab' + '12' + '3'                   string                'ab123'                                       'ab123'
i   x                                                          error                                         error        
j   "ab" + "cd"                         string              "abcd"                                            'abcd'  
k   'abc' * 2                           string               'abcabc'                                       'abcabc'
l   '1'*2 + '2' * 3                     string              '11222'                                           '11222'
m   1 * 2 + '3' * 2                     string               '3+'33'                                            error
n   'A' ** 2                            string                 error                                             error   
o   'bc' % 2                            string               error                                                error  
p   'bc' / 2                                string             error                                            error

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''