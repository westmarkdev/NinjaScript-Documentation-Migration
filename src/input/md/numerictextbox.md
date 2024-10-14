










 


NumericTextBox







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?numerictextbox.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
NumericTextBox | [Previous page](ntwindow.htm)
[Return to chapter overview](add_on.htm)










NumericTextBox provides functionality for numeric text boxes to capture user input. This UI element can be defined in XAML for an AddOn if desired, with functionality and logic related to the text box defined in C#, as in the examples below.


 




|  |
| --- |
| Note:  For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm) |



 


 


NumericTextBox inherits from [System.Windows.Controls.Textbox](https://msdn.microsoft.com/en-us/library/system.windows.controls.textbox(v=vs.110).aspx), and the following additional properties can be accessed for an instance the class:


 




|  |  |
| --- | --- |
| Minimum | Determines the minimum value which can be entered |
| Maximum | Determines the maximum value which can be entered |
| ValueType | Determines the System.Type which can be accepted |





Examples
--------




| ns XAML Definition of the UI Element |
| --- |
| <!-- Create a grid in which to place the NumericTextBox -->
<grid>
   <!-- Define a NumericTextBox -->
   <t:numerictextbox grid.column="2" text="5" valuetype="{x:Type system:Int32}" width="50" x:name="daysBackSelector">
       <!-- Set the margins for the box -->
       <t:numerictextbox.margin>
           <thickness left="{StaticResource MarginButtonLeft}" right="{StaticResource MarginBase}" top="{StaticResource PaddingColumn}"></thickness>
       </t:numerictextbox.margin>
   </t:numerictextbox>
</grid> |



 





| ns C# Code Handling Logic |
| --- |
| private NumericTextBox daysBack;
 
private DependencyObject LoadXAML()
{
       // Find days back selector
       daysBack = LogicalTreeHelper.FindLogicalNode(pageContent, "daysBackSelector") as NumericTextBox;
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
 
 
 



