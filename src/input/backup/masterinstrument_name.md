










 


Name







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?masterinstrument_name.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
Name | [Previous page](mergepolicy.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the NinjaTrader database name of an instrument. For example, "MSFT", "ES", "NQ" etc...


 


 


Property Value
--------------


A string representing the name of the instrument.



Syntax
------


Instrument.MasterInstrument.Name


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
         {
                 // Displays the master instrument's name at the bottom right of the chart
                 Draw.TextFixed(this, "tag1", Bars.Instrument.MasterInstrument.Name, TextPosition.BottomRight);
         } |




 


Additional Access Information
This property can be accessed without a null reference check in the OnBarUpdate() event handler. When the OnBarUpdate() event is triggered, there will always be an Instrument object. Should you wish to access this property elsewhere, check for null reference first. e.g. if (Instrument != null)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





 
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
 
 
 



