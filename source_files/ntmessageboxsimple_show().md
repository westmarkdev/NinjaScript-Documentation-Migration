










 


NTMessageBoxSimple.Show()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ntmessageboxsimple_show().htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
NTMessageBoxSimple.Show() | [Previous page](ntmenuitem.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


Creates a message box window.


 




|  |
| --- |
| Note: For more information on using MessageBox windows, please see [.NET MessageBox Class Documentation](https://docs.microsoft.com/en-us/dotnet/api/system.windows.messagebox?view=netframework-4.8) |



 


Method Return Value
-------------------


MessageBoxResult; an enum representing the button press used to close the MessageBox window


 


Syntax
------


NTMessageBoxSimple.Show(Window input, string messageTxt, string caption, MessageBoxButton buttonSet, MessageBoxImage icon)


 


 
Parameters
------------




|  |  |
| --- | --- |
| parent | A Window (DependencyObject) which represents the owning window |
| messageTxt | The message body of the MessageBox window |
| caption | The header of the MessageBox window |
| buttonSet | A MesageBoxButton enum determining the buttons used for the MessageBox window |
| icon | A MesageBoxImage enum determining the icon used for the MessageBox window |




 


Examples
--------




| ns |
| --- |
| // Create a MessageBox window from a Chart
ChartControl.Dispatcher.InvokeAsync(new Action(() =&gt; {      
   NinjaTrader.Gui.Tools.NTMessageBoxSimple.Show(Window.GetWindow(ChartControl.OwnerChart as DependencyObject), "Message Body", "Message Header", MessageBoxButton.OK, MessageBoxImage.None);
})); |



 




| ns |
| --- |
| // Create a MessageBox window from a button press in an AddOn
private void OnMenuItemClick(object sender, RoutedEventArgs e)
{
    NinjaTrader.Gui.Tools.NTMessageBoxSimple.Show(Window.GetWindow(e.Source as DependencyObject), "Message Body", "Message Header", MessageBoxButton.OK, MessageBoxImage.None);
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
 
 
 



