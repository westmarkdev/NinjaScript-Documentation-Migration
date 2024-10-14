










 


CurrentBar







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?currentbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnBarUpdate()](onbarupdate.htm) &gt;
CurrentBar | [Previous page](count.htm)
[Return to chapter overview](onbarupdate.htm)










Definition
----------


A number representing the current bar in a Bars object that the OnBarUpdate() method in an indicator or strategy is currently processing. For example, if a chart has 100 bars of data, the very first bar of the chart (left most bar) will be number 0 (zero) and each subsequent bar from left to right is incremented by 1.


 




|  |
| --- |
| Note:    In [multi series](multi-time_frame__instruments.htm) processing, the [CurrentBars](currentbars.htm) starting value will be -1 until all series have processed the first bar. |



 



Property Value
--------------


An int value that represents the current bar.


 


Syntax
------


CurrentBar


 



Examples
--------




| ns |
| --- |
| // OnBarUpdate method
protected override void OnBarUpdate()
{
     // Evaluates to make sure we have at least 20 or more bars
     if (CurrentBar &lt; 20)
         return;
 
     // Indicator logic calculation code...
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
 
 
 



