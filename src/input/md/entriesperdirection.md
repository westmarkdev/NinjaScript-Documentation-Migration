










 


EntriesPerDirection







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?entriesperdirection.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
EntriesPerDirection | [Previous page](disconnectdelayseconds.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines the maximum number of entries allowed per direction while a position is active based on the [EntryHandling](entryhandling.htm) property.


 




|  |
| --- |
| Note:  This property ONLY applies to Managed order methods.  When [IsUnmanaged](isunmanaged.htm) is set to true, Entry Handling properties will be hidden from the UI. |



 


 


Property Value
--------------


An int value represents the maximum number of entries allowed.  Default value is 1.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


EntriesPerDirection


 



Examples
--------




| ns If an open position already exists, subsequent EnterLong() calls are ignored.  |
| --- |
| // Example #1 
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         EntriesPerDirection = 1;
         EntryHandling = EntryHandling.AllEntries;
     }
}
 
protected override void OnBarUpdate()
{
     if (CrossAbove(SMA(10), SMA(20), 1)
         EnterLong("SMA Cross Entry");
 
     if (CrossAbove(RSI(14, 3), 30, 1)
         EnterLong("RSI Cross Entry);
} |



 


 




| ns EnterLong() will be processed once for each uniquely named entry. |
| --- |
| // Example #2
protected override void OnStateChange()
{
     EntriesPerDirection = 1;
     EntryHandling = EntryHandling.UniqueEntries;
}
 
protected override void OnBarUpdate()
{
     if (CrossAbove(SMA(10), SMA(20), 1)
         EnterLong("SMA Cross Entry");
 
     if (CrossAbove(RSI(14, 3), 30, 1)
         EnterLong("RSI Cross Entry);
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
 
 
 



