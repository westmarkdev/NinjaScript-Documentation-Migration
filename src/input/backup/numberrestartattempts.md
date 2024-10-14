










 


NumberRestartAttempts







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?numberrestartattempts.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
NumberRestartAttempts | [Previous page](iswaituntilflat.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines the maximum number of restart attempts allowed within the last x minutes defined in [RestartsWithinMinutes](restartswithinminutes.htm) when the strategy experiences a connection loss. If restart attempts exceeds this property within a time span shorter than or equal to RestartsWithinMinutes, then the strategy will be stopped and no further attempts will occur. The purpose of these settings is to stop the strategy should your connection be unstable and incapable of maintaining a consistent connected state.


 


Property Value
--------------


An int value represents the maximum number of restart attempts.  Default value is set to 4.


 


Syntax
------


NumberRestartAttempts


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Only allow the strategy to restart 4 times within the MaxRestartMinutes time span
         // If disconnected more than 4 times within that time span, stop the strategy and do not
         // attempt any further restarts.
         NumberRestartAttempts = 4;
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
 
 
 



