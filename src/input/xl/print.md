










 


Print()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?print.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
Print() | [Previous page](playsound.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Converts object data to a string format and appends the specified value as text to the NinjaScript [Output window](output.htm). Printing data to the NinjaScript Output window is a useful debugging technique to verify values while developing your custom NinjaScript object.


 




|  |
| --- |
| Notes:  The Print() method only targets the Output tab recently specified by set [PrintTo](printto.htm) property. |





Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


Print(object value)


 




|  |
| --- |
| Warning:  High frequency of Print() method calls can represent a performance hit on your PC. Please see the NinjaScript section of the [Performance Tips](performance_tips2.htm) article for more information. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| value | The object to print to the output window |



 


 




|  |
| --- |
| Tips:
1.You can format prices aligned for easier debugging by using the ToString() method.  E.g., Low[0].ToString("0.00") forces the format from 12.5 to 12.50.  Low[0].ToString("0.000") forces 12.500.2.You can format one or more objects in a specified string with the text equivalent of a corresponding object's value for better maintainability using the .NET [string.Format()](https://msdn.microsoft.com/en-us/library/system.string.format%28v=vs.110%29.aspx) method.  Please see the examples below. |





Examples
--------




| ns Passing objects directly to Print() method |
| --- |
| protected override void OnBarUpdate()
{
   // Generates a message
   Print("This is a message");
     //Output:  This is a message
 
   Print("The high of the current bar is : " + High[0]);
         //Output:  The high of the current bar is : 2112.75
 
   // Prints the current bar SMA value to the output window
   Print(SMA(Close, 20)[0]);
    
     //Output: 2110.5;
} |



 


 




| ns Passing string.Format() directly to Print() method |
| --- |
| protected override void OnBarUpdate()
{
   //Format and Print each bar value to the output window
   Print(string.Format("{0};{1};{2};{3};{4};{5}", Time[0], Open[0], High[0], Low[0], Close[0], Volume[0]));
     //Output:  2/24/2015 11:01:00 AM;2110.5;2110.5;2109.75;2110;1702
} |



 


 




|  |
| --- |
| ns Storing and reusing variables in Print() method |
| protected override void OnBarUpdate()
{
   //store the Close[0] value in a variable which can be printed later*        
   double myValue = Close[0];      
 
   //create and store a custom error message
   string myError = string.Format("Error on Bar {0}, value {1} was not expected", CurrentBar, myValue);         
 
   //*Storing the value adds better reusability of the error message above for other objects  
   //For example later down on line #19 we replace myValue = Close[0] with another double value Low[0]
   //This allows you to reuse the custom error formatted above on line #7 without repeating yourself
 
   //our first test case, if true print our error
   if(myValue &gt; High[0])            
     Print(myError);
     //Output: Error on Bar 233, value 1588.25 was not expected
 
   //reassign myValue
   myValue = Low[0];
 
   //our second test case (now uses Low[0]), if true print our error
   if(myValue &gt; Close[0])
     Print(myError);
     //Output: Error on Bar 57, value 1585.5 was not expected
} |






 
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
 
 
 



