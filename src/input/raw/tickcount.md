










 


TickCount







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tickcount.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
TickCount | [Previous page](percentcomplete.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the total number of ticks of the current bar processing.


 




|  |
| --- |
| Note:  For historical usage, you must use Calculate.OnEachTick with [TickReplay](developing_for__tick_replay.htm) enabled; otherwise a value of 1 will returned. |



 


 


Property Value
--------------


A long value that represents the total number of ticks of the current bar.


 


Syntax
------


Bars.TickCount



Examples
--------




| ns |
| --- |
| // Prints the tick count to the output window
Print("The tick count of the current bar is " + Bars.TickCount.ToString()); |






 
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
 
 
 



