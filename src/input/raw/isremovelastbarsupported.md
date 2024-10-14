










 


IsRemoveLastBarSupported







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isremovelastbarsupported.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
IsRemoveLastBarSupported | [Previous page](icon_barstype.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Determines if the bars type can use the [RemoveLastBar()](removelastbar.htm) method when true, otherwise an exception will be thrown. Bar Types which use remove last bar concepts CANNOT be used with [Tick Replay](tick_replay.htm), and as a result Tick Replay will be disabled on the UI when IsRemoveLastBarSupported is set to true.





|  |
| --- |
| Note:  This property is read-only, but may be overridden in a custom bar type.   |



 


 


Syntax
------


IsRemoveLastBarSupported


 


Property value
--------------


A bool determining if the BarsType can remove the last; default value is false.



Examples
--------




| ns |
| --- |
| // allows RemoveLastBar() to be called
public override bool IsRemoveLastBarSupported { get { return true; } } |






 
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
 
 
 



