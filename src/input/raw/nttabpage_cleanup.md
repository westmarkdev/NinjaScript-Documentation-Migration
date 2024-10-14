










 


CleanUp()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?nttabpage_cleanup.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NTTabPage Class](nttabpage_class.htm) &gt;
CleanUp() | [Previous page](nttabpage_class.htm)
[Return to chapter overview](nttabpage_class.htm)










Definition
----------


Unregisters LinkControls ([IInstrumentProvider](iintervalprovider_interface.htm) [IIntervalProvider)](iintervalprovider_interface.htm) and calls Cleanup() on ICleanable controls on the NTTabPage. Override this to, e.g., unsubscribe from events or perform any other cleanup operations when the tab is closed.


 




|  |
| --- |
| Note:  When overriding Cleanup(), it is strongly recommended when you call base.Cleanup() which ensures any link controls are also unregistered.  The base implementation will also handle cleaning up any controls which implement ICleanable: [AccountSelector](accountselector.htm), [AtmStrategySelector](atmstrategyselector.htm), [InstrumentSelector](instrumentselector.htm), [IntervalSelector](intervalselector.htm), [TifSelector](tifselector.htm) |



 


 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


public override void Cleanup()


{


}


 
Parameters
------------


This method does not accept any parameters


 


Examples
--------




| ns |
| --- |
| public override void Cleanup()
{
   // unregister from any custom events
   Connection.ConnectionStatusUpdate                   -= OnConnectionStatusUpdate;
   
   // a call to base.Cleanup() will loop through the visual tree looking for all ICleanable children
   // i.e., AccountSelector, AtmStrategySelector, InstrumentSelector, IntervalSelector, TifSelector,
   // as well as unregister any link control events
 
   base.Cleanup();
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
 
 
 



