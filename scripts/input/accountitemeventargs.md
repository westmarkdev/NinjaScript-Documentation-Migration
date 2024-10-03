










 


AccountItemEventArgs







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?accountitemeventargs.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [OnAccountItemUpdate()](onaccountitemupdate.htm) &gt;
AccountItemEventArgs | [Previous page](onaccountitemupdate.htm)
[Return to chapter overview](onaccountitemupdate.htm)










Definition
----------


AccountItemEventArgs contains [Account](account_class.htm)-related information to be passed as an argument to the [OnAccountItemUpdate(](onaccountitemupdate.htm)[)](accountitemupdate.htm) event.


 


 




|  |
| --- |
| Note:  For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm) |



 


The properties listed below are accessible from an instance of AccountItemEventArgs:


 




|  |  |
| --- | --- |
| Account | The Account for which OnAccountItemUpdate() was called |
| AccountItem | The [AccountItem](accountitem.htm) which has updated, resulting in the call to OnAccountItemUpdate() |
| Currency | The currency of the Account in question |
| Time | A DateTime object representing the time at which the change occurred |
| Value | The new value of the updated AccountItems |



 


Example
-------




| ns |
| --- |
| // This method is fired on any change of an AccountItem
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
       /* Dispatcher.InvokeAsync() is needed for multi-threading considerations. When processing events outside of the UI thread, and we want to
        influence the UI .InvokeAsync() allows us to do so. It can also help prevent the UI thread from locking up on long operations. */
       Dispatcher.InvokeAsync(() =&gt;
       {
           //Print which AccountItem changed, on which account, and the new value, using
           outputBox.AppendText(string.Format("{0}Account: {1}{0}AccountItem: {2}{0}Value: {3}",
               Environment.NewLine,
               e.Account.Name,
               e.AccountItem,
               e.Value));
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
 
 
 



