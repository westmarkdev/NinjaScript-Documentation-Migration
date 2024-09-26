










 


Formatting numbers







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?formatting_numbers.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Tips](tips.htm) &gt;
Formatting numbers | [Previous page](floating-point_arithmetic.htm)
[Return to chapter overview](tips.htm)










String formatting on numbers is very useful for creating readable output. This can be done through the use of the number object's ToString() method.


 


A common practice is printing out mathematical operations with the use of the ToString() method on the double object. What usually happens is the printing of a long string containing all the decimal places existing in the double. This sometimes makes output cluttered and hard to read. Luckily, C# has a robust set of string formatting options available to make the string more comprehendible.


 


Here is a list of common formatting options available in the ToString() method:




| ns |
| --- |
| double c = 10.25693;
Print("No formatting: " + c.ToString());
Print("Currency formatting: " + c.ToString("C"));
Print("Exponential formatting: " + c.ToString("E"));
Print("Fixed-point formatting: " + c.ToString("F2"));
Print("General formatting: " + c.ToString("G"));
Print("Percent formatting: " + c.ToString("P0"));
Print("Formatted to 2 decimal places: " + c.ToString("N2"));
Print("Formatted to 3 decimal places: " + c.ToString("N3"));
Print("Formatted to 4 decimal places: " + c.ToString("N4")); |



 


The corresponding output is as follows:




| ns |
| --- |
| No formatting: 10.25693
Currency formatting: $10.26
Exponential formatting: 1.025693E+001
Fixed-point formatting: 10.26
General formatting: 10.25693
Percent formatting: 1,026 %
Formatted to 2 decimal places: 10.26
Formatted to 3 decimal places: 10.257
Formatted to 4 decimal places: 10.2569 |



 


For custom formatting you can use the following:




| ns |
| --- |
| double phoneNumber = 9165551022;
Print("Phone number: " + phoneNumber.ToString("(###) ### - ####")); |



 


Corresponding output:




| ns |
| --- |
| Phone number: (916) 555 - 1022 |



 


For more information on general string formatting the Microsoft documentation may be of use. Many other resources can be found online through a Google search as well.


<https: base-types="" dotnet="" en-us="" learn.microsoft.com="" standard="" standard-numeric-format-strings="">
<https: base-types="" custom-numeric-format-strings="" dotnet="" en-us="" learn.microsoft.com="" standard=""> 





 
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
 
 
 



</https:></https:>