










 


Expiry







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?expiry.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt;
Expiry | [Previous page](exchange.htm)
[Return to chapter overview](instrument.htm)










Definition
----------


Indicates the expiration month of a futures contract.


 


Property Value
--------------


A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure representing the expiration month of a futures contract.


 


Syntax
------


Instrument.Expiry


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Print the expiry of the currently configured futures instrument
   Print(String.Format("You are viewing the {0} contract", Instrument.Expiry));
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
 
 
 



