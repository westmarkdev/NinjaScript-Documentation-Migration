










 


EntryHandling







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?entryhandling.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
EntryHandling | [Previous page](entriesperdirection.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Sets the manner in how entry orders will handle.


 




|  |
| --- |
| Note:  This property ONLY applies to Managed order methods.  When [IsUnmanaged](isunmanaged.htm) is set to true, Entry Handling properties will be hidden from the UI. |



 


 


Property Value
--------------


An enum which sets how the entry orders are handled.  Default value is EntryHandling.AllEntries.  Possible values include:


 




|  |  |
| --- | --- |
| EntryHandling.AllEntries | NinjaScript will process all [order entry methods](order_methods.htm) until the maximum allowable entries set by the [EntriesPerDirection](entriesperdirection.htm) property is reached while in an open position |
| EntryHandling.UniqueEntries | NinjaScript will process order entry methods until the maximum allowable entries set by the EntriesPerDirection property per each uniquely named entry |



 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


EntryHandling


 



Examples
--------




| ns Allow a maximum of two entries while a position is open |
| --- |
| // Example #1
protected override void OnStateChange() 
{
     if (State == State.SetDefaults)
     {
         EntriesPerDirection = 2;
         EntryHandling = EntryHandling.AllEntries;
     }
}
 
protected override void OnBarUpdate() 
{
     if (CrossAbove(SMA(10), SMA(20), 1)
         EnterLong("SMA Cross Entry");
} |



 


 




| ns EnterLong() will be processed once for each uniquely named entry. |
| --- |
| // Example #2
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         EntriesPerDirection = 1;
         EntryHandling = EntryHandling.UniqueEntries;
     }
}
 
protected override void OnBarUpdate()
{
     if (CrossAbove(SMA(10), SMA(20), 1)
         EnterLong("SMA Cross Entry");
 
     if (CrossAbove(RSI(14, 3), 30, 1)
         EnterLong("RSI Cross Entry");
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
 
 
 



