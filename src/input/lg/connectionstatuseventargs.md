










 


ConnectionStatusEventArgs







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?connectionstatuseventargs.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnConnectionStatusUpdate()](onconnectionstatusupdate.htm) &gt;
ConnectionStatusEventArgs | [Previous page](onconnectionstatusupdate.htm)
[Return to chapter overview](onconnectionstatusupdate.htm)










Definition
----------


ConnectionStatusEventArgs contains [Connection](connection.htm)-related information to be passed as an argument to the [OnConnectionStatusUpdate()](onconnectionstatusupdate.htm) event.


 


 




|  |
| --- |
| Note:  For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](addon_development_overview.htm) |



 


 


The properties listed below are accessible from an instance of ConnectionStatusEventArgs:


 




|  |  |
| --- | --- |
| Connection | The Connection object for which OnConnectionStatusUpdate() was called |
| Error | An ErrorCode thrown by the Connection object in question |
| NativeError | A string representing an error thrown by the connectivity provider |
| PreviousStatus | A ConnectionStatus object representing the status of the connection before this call to OnConnectionStatusUpdate() |
| Status | A ConnectionStatus object representing the new status of the connection  |
| PreviousPriceStatus | A ConnectionStatus object representing the status of the connection's price feed before this call to OnConnectionStatusUpdate() |
| PriceStatus | A ConnectionStatus object representing the new status of the connection's price feed |





Examples
--------




| ns |
| --- |
| // This method is fired on connection status events
private void OnConnectionStatusUpdate(object sender, ConnectionStatusEventArgs e)
{
   // For multi-threading reasons, work with a copy of the ConnectionStatusEventArgs to prevent situations in which the EventArgs may already be ahead of us while in the middle processing it.
   // This accomplishes the same goal as locking a collection to prevent in-flight changes from affecting outcomes
   ConnectionStatusEventArgs eCopy = e;
 
   /* Dispatcher.InvokeAsync() is needed for multi-threading considerations. When processing events outside of the UI thread, and we want to
    influence the UI .InvokeAsync() allows us to do so. It can also help prevent the UI thread from locking up on long operations. */
   Dispatcher.InvokeAsync(() =&gt;
   {
       outputBox.AppendText(string.Format("{1} Status: {2}",
               Environment.NewLine,
               eCopy.Connection.Options.Name,
               eCopy.Status));
   });   
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
 
 
 



