










 


Exchange







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?exchange.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt;
Exchange | [Previous page](instrument.htm)
[Return to chapter overview](instrument.htm)










Definition
----------


Indicates the current exchange of an instrument


 


Property Value
--------------


Represents the exchange which is selected for the current instrument.


 


Syntax
------


Instrument.Exchange


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Print the exchange of the currently configured instrument
   Print(String.Format("Configured instrument is on the {0} exchange", Instrument.Exchange));
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
 
 
 



