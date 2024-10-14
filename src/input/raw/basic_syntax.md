


Basic Syntax









 


Basic Syntax















NinjaScript is an extension to the powerful Microsoft C# language. The following syntax guide is a subset of the capabilities of the C# language. For tutorials and an online reference to the C# language, visit the [Microsoft Developer Network](https://msdn.microsoft.com/en-us/library/67ef8sbd.aspx).


 


Statements
----------


A statement is analogous to a complete sentence in the English language.


 


Example:


 


I like trading.


 


This is clear and easy to understand. Compared to:


 


I like.


 


Anyone reading this would not know what you like. This is not a complete sentence. The same logic applies to a C# statement, it forms a complete instruction that can be interpreted by the compiler.


 




| ns |
| --- |
| sum = 10 + 10; |



 


The above statement is complete since we are saying that the variable sum is equal to 10 plus 10. Notice that the statement ends with a semicolon ";" and not a period. In English, sentences end with a period, but in C#, statements end with a semicolon.


 


 


Building Blocks
---------------


Building blocks are analogous to paragraphs in the English language, in that they group statements together. In the programming world we call this a "Block of code". These blocks are delimited with curly braces "{}" like the following example:


 




| ns |
| --- |
| if (x == 5)
{
     Print("NinjaTrader");
     Print("NinjaScript");
} |



 


The above code block encloses two statements in curly braces.


 




|  |
| --- |
| Note: This is also referred to as "encapsulation." |



 


User Defined Comments
---------------------


You can add your own comments to your code.


 


Use the "//" characters for single line comments.


 




| ns |
| --- |
| // This line is a comment, and will not be executed with the rest of your code |



 


You can enclose several comment lines using the "/*" characters to start the comment block and then using the "*/" characters to end the comment block.


 




| ns |
| --- |
| /* These are comments to illustrate a multi line comment
block within NinjaScript */ |



 


Case Sensitivity
----------------


C# is a case-sensitive language, which means that "NinjaTrader" with a capital "N" is not the same as "ninjaTrader" with a lower-case "n".


 


 


Variables and Value Types
-------------------------


A variable is a place holder that stores information in computer memory. Because it points to a specific memory location, variables are unique, like mailing addresses. Use variables to store and access data. There are many variable types that you can use in the C# language. The following are a few of the basics:


 


string


Stores textual data


 


double


Stores floating point values


 


int (integer)


Stores whole number values


 


bool


Stores either true or false


 


object


Stores objects such as NinjaTrader indicators (in these cases, you would declare the variable type as the object type itself)


 


Declaring Variables
-------------------


To declare a variable in C# you must first declare its data type and then provide a unique name, and optionally assign a value.


 




| ns |
| --- |
| // Declaring a string variable
string myString = "NinjaTrader";
 
// Declaring a double variable
double myDouble = 2.5;
 
// Declaring an integer variable
int myInteger = 1;
 
// Declaring a bool variable
bool learningIsFun = true;
 
// Declaring an object type variable using a Simple Moving Average indicator
SMA mySMA = new SMA(Close, 20); |



 


In each of the above examples, you will notice that the equals character "=" is used to assign a value to the declared variable. In C#, this character is called the "assignment operator," because it is used to assign values or references to variables.


 


Operators
---------


C# provides a large set of operators, which are symbols that specify which operations to perform in a statement. The following is a subset of common operators.


 


Arithmetic




|  |  |
| --- | --- |
| + | addition |
| - | subtraction |
| * | multiplication |
| / | division |



 




| ns |
| --- |
| // Example of using arithmetic operators
int myInteger = 0;
myInteger = 5 + (3 * 4);
Print(myInteger.ToString()); |



 


The above example would print a value of 17 to the NinjaScript Output window. The System.Math class, which is part of the .NET Framework, provides additional math functions.


For example:


 




| ns |
| --- |
| // Example of using the ABS method of the System.Math class 
double myDouble = Math.Abs(5 - 6); 
Print(myDouble.ToString()); |



 


The code above would print a value of 1 to the NinjaScript Output window. 


 


Logical




|  |  |
| --- | --- |
| &amp;&amp; | AND |
| || | OR |



 




| ns |
| --- |
| // Example of using logical operators
int myInteger = 3;
string myString = "NinjaTrader";
if (myInteger == 3 &amp;&amp; myString == "NinjaTrader")
{
     Print("true");
} |



 


The above example will print "true" to the NinjaScript Output window if the variable myInteger is equal to 3 and also (&amp;&amp; operator used) the variable myString is equal to NinjaTrader.


 


Relational




|  |  |
| --- | --- |
| == | equal to |
| != | not equal to |
| &lt; | less than |
| &gt; | greater than |
| &lt;= | less than or equal to |
| &gt;= | greater than or equal to |



 




| ns |
| --- |
| // Example of using relational operator
string myString = "NinjaTrader";
if (myString != "trading")
{
   Print("Variable myString does not equal trading");
}
 
// Second example of using a relational operator in conjunction with logical operator
double myDouble = 1000.25;
 
if (myDouble &lt; 1000 || myDouble &gt; 1001)
{
     // Note that since myDouble does not satisfy the if-statement, no printout will be seen
     Print("Variable myDouble is between 1000 and 1001");
} |



 


Assignment




|  |  |
| --- | --- |
| = | equals |
| += | x += y is equivalent to x = x + y |
| -= | x -= y is equivalent to x = x - y |
| *= | x *= y is equivalent to x = x * y |
| /= | x /= y is equivalent to x = x / y |



 


Conditional


 


?:


 




| ns |
| --- |
| // Example of a conditional operator
int myInteger = (10 &gt; 12 ? 3 : 4);
Print(myInteger.ToString()); |



 


The above conditional statement says "assign the value 3 to the variable myInt if 10 is greater than 12, else assign the value 4 to the variable myInt." The example will then print the value of 4 to the NinjaScript Output window, since 10 is not greater than 12.


 


String Concatenation
--------------------


"String Concatenation" refers to appending one string onto another. To do this, use the "+" character.


 




| ns |
| --- |
| // Example of string concatenation
string wordOne = "Ninja";
string wordTwo = "Trader";
Print(wordOne.ToString() + wordTwo.ToString()); |



 


The above example would print out "NinjaTrader" to the NinjaScript Output window.





 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



