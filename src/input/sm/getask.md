










 


GetAsk()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getask.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetAsk() | [Previous page](barssincenewtradingday.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the ask price value at a selected absolute bar index value.  


 




|  |
| --- |
| Notes: 
 
•This method does NOT return the current real-time asking price, but rather the historical / real-time asking price at the desired index.  For obtaining the current real-time asking price, please use [GetCurrentAsk](getcurrentask.htm)().•This method returns expected values when 1 tick bid / ask stamped data is used and available from [your provider](data_by_provider.htm). |



 


 


Method Return Value
-------------------


A double value that represents the asking price at the desired bar index.



Syntax
------


Bars.GetAsk(int index)


 


Parameters
----------




|  |  |
| --- | --- |
| index | The absolute bar index value used |



 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // If the Highs of the two most recent bars are falling, place a long stop market order 
   // at the Ask price 
   if (High[0] &lt; High[1] &amp;&amp; High[1] &lt; High[2])
   {
       EnterLongStopMarket(Bars.GetAsk(CurrentBar));
   }
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
 
 
 



