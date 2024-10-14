










 


PercentComplete







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?percentcomplete.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
PercentComplete | [Previous page](istickreplay.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns a value indicating the percentage complete of the real-time bar processing.


 




|  |
| --- |
| Notes:  
1.Since a historical bar is complete, values during State.Historical should be ignored (also the case with [TickReplay](developing_for__tick_replay.htm) bars)2.Some [BarsTypes](bars_type.htm) may not be compatible with the PercentComplete property. In these cases, a value of 0 always returns (e.g.,  Range, Renko, Point &amp; Figure, Kagi, LineBreak, and some other 3rd party bars types) |



 


 


Property Value
--------------


A double value representing a percent e.g. a value of .5 indicates the bar was at 50%.  This property is read-only.


 


Syntax
Bars.PercentComplete
---------------------------





|  |
| --- |
| Tip:  If you are developing a custom BarsType, please use the [GetPercentComplete()](getpercentcomplete.htm) method used to calculate the value returned by PercentComplete |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   if(State == State.Realtime)
   {
     Draw.TextFixed(this, "barstatus", Bars.PercentComplete.ToString("P2"), TextPosition.BottomRight);
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
 
 
 



