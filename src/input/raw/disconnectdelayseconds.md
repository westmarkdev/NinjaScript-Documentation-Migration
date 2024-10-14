










 


DisconnectDelaySeconds







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?disconnectdelayseconds.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
DisconnectDelaySeconds | [Previous page](defaultquantity.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines the amount of time a disconnect would have to last before [connection loss handling](connectionlosshandling.htm) takes action. 


 


Property Value
--------------


An int value represents the time required for a disconnect to last before connection loss handling actions will occur.  Default value is 10.


 


Syntax
------


DisconnectDelaySeconds


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Disconnect has to be at least 10 seconds
         DisconnectDelaySeconds = 10;
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
 
 
 



