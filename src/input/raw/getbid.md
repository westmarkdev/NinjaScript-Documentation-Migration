﻿










 


GetBid()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getbid.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetBid() | [Previous page](getbar.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the bid price value at a selected absolute bar index value.


 




|  |
| --- |
| Notes: 
 
•This method does NOT return the current real-time bid price, but rather the historical / real-time bid price at the desired index.  For obtaining the current real-time bid price, please use [GetCurrentBid()](getcurrentbid.htm).•This method returns expected values when 1 tick bid / ask stamped data is used and available from [your provider](data_by_provider.htm). |



 


 


Method Return Value
-------------------


A double value that represents the biding price at the desired bar index.



Syntax
------


Bars.GetBid(int index)


 


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
   if (Low[0] &gt; Low[1] &amp;&amp; Low[1] &lt; Low[2])
   {
     EnterShortStopMarket(Bars.GetBid(CurrentBar));
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
 
 
 


