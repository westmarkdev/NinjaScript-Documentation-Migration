










 


CountIf()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?countif.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
CountIf() | [Previous page](approxcompare.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Counts the number of instances the test condition occurs over the look-back period expressed in bars.


 




|  |
| --- |
| Note: This method does NOT work on [multi-series](multi-time_frame__instruments.htm) strategies and indicators.  |



 


 


Method Return Value
-------------------


An int value representing the number of occurrences found


 


Syntax
------


CountIf(Func<bool> condition, int period)  

 


Parameters
----------




|  |  |
| --- | --- |
| condition | A true/false expression |
| period | Number of bars to check for the test condition |



 


 




|  |
| --- |
| Tip:  The syntax for the "condition" parameter uses [lambda expression](http://msdn.microsoft.com/en-us/library/bb397687.aspx) syntax |



 


 


Examples
--------




| ns |
| --- |
| // If in the last 10 bars we have had 8 up bars then go long
if (CountIf(() =&gt; Close[0] &gt; Open[0], 10) &gt; 8)
     EnterLong(); |






 
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
 
 
 



</bool>