










 


GetNextExpiry()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getnextexpiry.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
GetNextExpiry() | [Previous page](masterinstrument_name.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Returns the current futures expiry compared to the time of the input value used for the method.



Method Return Value
-------------------


A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure


 


Syntax
------


Bars.Instrument.MasterInstrument.GetNextExpiry(DateTime afterDate)


 


Parameters
----------




|  |  |
| --- | --- |
| afterDate | A DateTime value representing to be compared |



 


Examples
--------




| ns |
| --- |
| // Indicates what the current expiry is in the bottom right of the chart
Draw.TextFixed(this, "tag1", "The current expiry is " + Bars.Instrument.MasterInstrument.GetNextExpiry(DateTime.Now).ToString("MM-yy"), TextPosition.BottomRight); |






 
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
 
 
 



