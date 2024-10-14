










 


Export Problems







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?export_problems.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Distribution](distribution.htm) &gt;
Export Problems | [Previous page](remove-ninjascript-assembly.htm)
[Return to chapter overview](distribution.htm)



[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









If you are having difficulties exporting NinjaScript it could be due to one of the following reasons:


![tog_minus](tog_minus.gif)        [NinjaScript Compile Error](javascript:HMToggle('toggle','ninjascriptCompileError','ninjascriptCompileError_ICON'))




|  |
| --- |
| Export_Problems_1
 
If you receive the above error, you will need to compile your NinjaScript error-free before you can export. To see if your NinjaScript file is error free, open the NinjaScript Editor (Tool &gt; Edit NinjaScript) and press F5 to compile. If you are trying to check a NinjaScript Strategy created from the Strategy Wizard you can do the same by finishing the wizard and seeing if you receive the “Strategy successfully generated” message.
 
If you receive any errors when compiling you will need to address them before exporting. |



![tog_minus](tog_minus.gif)        [.NET Referencing](javascript:HMToggle('toggle','netReferencing','netReferencing_ICON'))




|  |  |
| --- | --- |
| Export_Problems_2
 
If you are able to compile without errors and still experience exporting difficulties like the one above, check to see if you receive an error similar to this in the Control Center logs:
 
"3/6/2014 9:25:30 AM|2|4|Error compiling export assembly: C:\Users\NinjaTrader\Documents\NinjaTrader 8\bin\Custom\Indicator\MyCustomIndicator.cs(42,18) : error CS0118: NinjaTrader.Indicator.SMA is a type but is used like a variable"
 
Note: This error may have a different error code and message depending on which variant of .NET you have installed. An error message indicative of this issue would include an indicator name without quotation marks.
 
If you experience this error, please follow this procedure:
 
1. Take note of which indicator is referenced by the error. In the above example, it is the SMA
2. Go to your NinjaScript Export utility. (Tools &gt; Export &gt; NinjaScript...)
3. After press "add" select “System indicators” from the "Type" drop down
 
Export_Problems_3
 
4. Add the indicator that was referenced in the error to the export list along with your custom NinjaScript by pressing the &gt; button
 
Export_Problems_4
 
5. Press the “Export” button to create your NinjaScript Archive File. If you receive the same error again, repeat this procedure until you add all the referenced system indicators and are able to successfully export your custom NinjaScript. 
 


|  |
| --- |
| Note: If the indicator referenced in the error is another custom indicator you will need to follow the same procedure to add the custom indicator. |


 |






 
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
 
 
 


HMInitToggle('ninjascriptCompileError\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'ninjascriptCompileError\',\'ninjascriptCompileError\_ICON\')');
HMInitToggle('ninjascriptCompileError','hm.type','dropdown','hm.state','0');
HMInitToggle('netReferencing\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'netReferencing\',\'netReferencing\_ICON\')');
HMInitToggle('netReferencing','hm.type','dropdown','hm.state','0');



