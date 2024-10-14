










 


IsDataSeriesRequired







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isdataseriesrequired.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnBarUpdate()](onbarupdate.htm) &gt;
IsDataSeriesRequired | [Previous page](currentbar.htm)
[Return to chapter overview](onbarupdate.htm)










Definition
----------


Determines if a Data Series is required for calculating this NinjaScript object.  When set to false, data series related properties will not be displayed on the UI when configuring. 


 




|  |
| --- |
| Note:  When set to false, methods and properties which are dependent on Bars will NOT be used.  This means you will not receive any calls to OnBarUpdate() or be able to access historical bar prices. |



 


 


Property Value
--------------


This property returns true if the NinjaScript requires a Data Series; otherwise, false.  Default value is true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


IsDataSeriesRequired


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         IsDataSeriesRequired = false;
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
 
 
 



