










 


IsAdoptAccountPositionAware







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isadoptaccountpositionaware.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IsAdoptAccountPositionAware | [Previous page](includetradehistoryinbacktest.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines if the strategy is programmed in a manner capable of handling  real-world account positions. Once set to true, your strategy's "[Start behavior](startbehavior.htm)" options will include an additional parameter named "Adopt account position" which can bet set at run-time.  Only set to true if you have specifically programmed your strategy to be able to adopt account positions. 


 


Property Value
--------------


This property returns true if the strategy can adopt account positions; otherwise, false. Default is set to false.


 




|  |
| --- |
| Note:  This property should ONLY be set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults. |




Syntax
------


IsAdoptAccountPositionAware


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         IsAdoptAccountPositionAware = true;
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
 
 
 



