










 


Instruments







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?instruments_ninjascript.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Instruments | [Previous page](removedrawobjects.htm)
[Return to chapter overview](common.htm)










Definition
----------


A collection of [Instrument](instrument.htm) objects currently used by a script.


 


Property Value
--------------


An array of Instrument objects


 


Syntax
------


Instruments[]


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.DataLoaded)
   {
       // Print all instruments which have been loaded
       foreach (Instrument i in Instruments)
       {
           Print(i.FullName);
       }
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
 
 
 



