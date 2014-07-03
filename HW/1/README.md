#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
Because computers only undersand two states on and off.
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
11001001
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
b = 11 = 1101
5 = 1010
b5 = 11011010
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
array
```

(b) What type of data is returned by this function? **(1 mark)**
```
boolean
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
line 3
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
an error that completly stops the code from working because the computer cannot understand what it is being told.
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
line 4 it is making the variable a different number each time. it should be: tot <- tot + num[x]
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
runtime error, and error thjat stop the program working in the middle of the code. e.g putting == instead of = in an equation.
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
 bound = N-1
    for i from 1 to N
        newbound = 0
        for j from 0 to bound
           if a[j] > a[j + 1]
              swap( a[j], a[j + 1] )
              newbound = j - 1
        bound = newbound
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: were all the devices are all connected by one cable or 'backbone'

Advantages: easy to stepup

Disadvantages: if the main cabel gets damaged the whole network goes down
```

**Ring Topology (6 marks)**
```
Describe: each device is connected to two others forming a ring

Advantages: fast to transfer data

Disadvantages: if any device is faulty the whole network goes down.
```

**Star Topology (6 marks)**
```
Describe: all the devices are connected to one centeral hub by seperate cables.

Advantages: very reliable it is not very easy to break.

Disadvantages: expensive to set up.
```
