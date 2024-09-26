










 


RemoveLastBar()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?removelastbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
RemoveLastBar() | [Previous page](ondatapoint.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Removes the last data point for the Bars Type.  There may be cases where your custom bar type may need to amend the last values added on a bar that has already closed.  Calling RemoveLastBar() will remove the last points for that bar type and allow you to call AddBar() with the updated values.





|  |
| --- |
| Notes:  
•In order to use this method, the [IsRemoveLastBarSupported](isremovelastbarsupported.htm) method must be true.  •RemoveLastBar() CANNOT be used with [TickReplay](tick_replay.htm) |



 


 


Syntax
------


RemoveLastBar(Bars bars)


 


Parameters
----------




|  |  |
| --- | --- |
| bars | The Bars object of your bars type |



 



Examples
--------




| ns |
| --- |
| RemoveLastBar(bars); |






 
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
 
 
 



