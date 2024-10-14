










 


Count







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iseries_count.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt;
Count | [Previous page](iseries_volumes.htm)
[Return to chapter overview](iseriest.htm)










Definition
----------


Indicates the number total number of values in the ISeries<t> array.  This value should always be in sync with the [CurrentBars](currentbars.htm) array for that series.


 


Method Return Value
-------------------


A int representing the total size of the series


 


Syntax
------


Count


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   Print("Input count: " + Input.Count);
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
 
 
 



</t></t></t>