










 


ApproxCompare()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?approxcompare.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
ApproxCompare() | [Previous page](market_data.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Compares two double or float values for equality or being greater than / less than the compared to value.


 




|  |
| --- |
| Note: Comparing for being greater than / less is done using an epsilon value of 1E19 |



 


Method Return Value
-------------------


An int value representing the outcome of the comparison. Returns 0 if values are equal, 1 if value1 is greater than value2. -1 if value1 is less than value2.


 


Syntax
------


this.ApproxCompare(this double double1, double double2)  

this.ApproxCompare(this float float1, double float2)  

 


Parameters
----------




|  |  |
| --- | --- |
| double1 / float1 | First value to compare against (not actually passed in) |
| double2 / float2 | Second passed in value to compare against |



 




|  |
| --- |
| Tip:  Main use would be using it for equality comparisons to circumvent running into floating point considerations, value compares for &lt; or &gt; could be usually done more straightforward directly. |



 


 


Examples
--------




| ns |
| --- |
|  | // Build the High / Low difference and if 0 sets the indicator main Value series to 0
if ((High[0] - Low[0]).ApproxCompare(0) == 0)
   Value[0] = 0; |



 





 
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
 
 
 



