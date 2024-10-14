










 


AttachedTo







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?attachedto.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
AttachedTo | [Previous page](anchors.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


An object which holds information regarding where the drawing tool is attached.


 


Available Properties
--------------------




|  |  |
| --- | --- |
| AttachedToType | An enum representing the type of object the drawing to is attached.  Possible values are:
•Bars - The chart bars of the parent chart•GlobalInstrument - The bars of an instrument crossed all charts•Indicator - A NinjaScript indicator•Strategy - A NinjaScript strategy |
| ChartObject | A ChartObject interface such an indicator, strategy, chart bars |
| DisplayName | A string value indicating the name of the object the drawing tool is attached |
| Instrument | The [Instrument](instrument.htm) that the drawing tool is attached |





Syntax
------


AttachedTo


 


 


Examples
--------




|  |
| --- |
| ns |
| if (AttachedTo.AttachedToType == AttachedToType.Indicator)
   // do something |






 
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
 
 
 



