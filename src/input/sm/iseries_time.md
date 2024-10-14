










 


Time







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iseries_time.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [TimeSeries<datetime>](timeseries.htm) &gt;
Time | [Previous page](timeseries.htm)
[Return to chapter overview](timeseries.htm)










Definition
----------


A collection of historical bar time stamp values.


 


Property Value
--------------


An ISeries<datetime> object.


 


Syntax
------


Time  

Time[int barsAgo] (returns a [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure)


 



Examples
--------




| ns |
| --- |
| // Prints the current bar time stamp
Print(Time[0].ToString());
 
// Checks if current time is greater than the bar time stamp
if (DateTime.Now.Ticks &gt; Time[0].Ticks)
     Print("Do something"); |






 
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
 
 
 



</datetime></datetime></t></datetime></t>