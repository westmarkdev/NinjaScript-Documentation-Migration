










 


FullName







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?instrument_fullname.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt;
FullName | [Previous page](expiry.htm)
[Return to chapter overview](instrument.htm)










Definition
----------


Indicates the full NinjaTrader name of an instrument. For futures, this would include the expiration date. The September S&amp;P 500 Emini contract full name is "ES 09-16".


 


Property Value
--------------


A string representing the full name of the instrument.


 


Syntax
------


Instrument.FullName


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Print the full name (including contract month) of the configured instrument
   Print(String.Format("{0} is being used as the input series", Instrument.FullName));
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
 
 
 



