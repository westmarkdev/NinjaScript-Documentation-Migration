










 


Disconnect()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?disconnect.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Connection](connection_class.htm) &gt;
Disconnect() | [Previous page](connectionstatusupdate.htm)
[Return to chapter overview](connection_class.htm)










Definition
----------


Disconnects from the data connection.


 


Syntax
------


<connection>.Disconnect()


 


 


Example
-------




| ns |
| --- |
| private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
   // If an execution triggers after 9pm, disconnect from the account's data source
   if (e.Time &gt; new DateTime(now.Year, now.Month, now.Day, 21, 0, 0))
       myAccount.Connection.Disconnect();
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
 
 
 



</connection>