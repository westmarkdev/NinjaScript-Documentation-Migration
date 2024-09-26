










 


TimeSeries<datetime>







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?timeseries.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt;
TimeSeries<datetime> | [Previous page](weighteds.htm)
[Return to chapter overview](iseriest.htm)










Definition
----------


Represents historical time stamps as an ISeries<datetime> interface which can be used for custom NinjaScript object calculations.





|  |
| --- |
| Note:  In most cases, you will access the historical time series using a core event handler such as OnBarUpdate.  For more advance developers, you may find situations where you wish to access historical time series outside of the core event methods, such as your own custom mouse click.  In these advanced scenarios, you may run into situations where the barsAgo pointer is not in sync with the current bar, which may cause errors when trying to obtain this information.  In those cases, use the Bars.Get...() methods with the absolute bar index, e.g., [Bars.GetTime()](gettime.htm), etc. |



 


 


Single ISeries<datetime>
------------------------




|  |  |
| --- | --- |
| Time | A collection of historical bar time stamp values. |





Multi-Time Frame ISeries<datetime>
----------------------------------




|  |  |
| --- | --- |
| Times | Holds an array of ISeries<datetime> objects holding historical bar times |



 





 
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
 
 
 



</datetime></datetime></datetime></datetime></datetime></t></datetime></datetime></t>