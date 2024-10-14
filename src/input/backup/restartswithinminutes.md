










 


RestartsWithinMinutes







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?restartswithinminutes.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
RestartsWithinMinutes | [Previous page](realtimeerrorhandling.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines within how many minutes the strategy will attempt to restart.  The strategy will only restart off a reestablished connection when there have been fewer restart attempts than [NumberRestartAttempts](numberrestartattempts.htm) in the last NumberRestartAttempts time span. The purpose of these settings is to stop the strategy should your connection be unstable and incapable of maintaining a consistent connected state.


 


Property Value
--------------


An int value representing the maximum number of minutes in the time span in which restart attempts have to be less than NumberRestartAttempts for a strategy to be restarted when a connection is reestablished. Default value is set to 5.


 


Syntax
------


RestartsWithinMinutes


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         /* Allow for restarting the strategy only if there were less restart attempts than
          MaxRestartAttempts within the last 5 minutes */
         RestartsWithinMinutes = 5;
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
 
 
 



