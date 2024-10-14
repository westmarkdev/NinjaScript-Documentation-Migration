










 


SupportsAlerts







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?supportsalerts.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
SupportsAlerts | [Previous page](onmouseup.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Determines if the drawing tool can be used for manually configured alerts through the UI.



Property Value
--------------


A bool which when true determines that user can setup an alert based off this drawing tool;  otherwise false. 


 




|  |
| --- |
| Note:  This property is false by default and MUST be overridden upon initialization to allow for manually configured alerts.  You cannot set this during run-time. |



 


 


Syntax
------


SupportsAlerts
--------------



You may choose to override this property using the following syntax:



public override bool SupportsAlerts 


 


 


Examples
--------




| ns |
| --- |
| public override bool SupportsAlerts { get { return true; } } |






 
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
 
 
 



