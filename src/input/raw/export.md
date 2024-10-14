










 


Export







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?export.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Distribution](distribution.htm) &gt;
Export | [Previous page](import.htm)
[Return to chapter overview](distribution.htm)



[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









You can export NinjaScript for others to import in several formats:   

 


•Source files - NinjaScript source files that can be imported and edited by others 

•Assemblies - A compiled assembly (DLL) of NinjaScript that "hides" your source code. This can be further [protected by SecureTeam's Agile.NET](protection_dll_security.htm) to prevent theft of your intellectual property.

![tog_minus](tog_minus.gif)        [Exporting NinjaScript as Source Files](javascript:HMToggle('toggle','ExportingninjascriptAsSourceFiles','ExportingninjascriptAsSourceFiles_ICON'))




|  |  |  |
| --- | --- | --- |
| You may want to provide other NinjaTrader users with source files of your NinjaScript in a format where they are able to view and edit them.
 
1.From the Control Center window select the menu Tools &gt; Export &gt; NinjaScript... to open the "Export NinjaScript" dialog window  
2.Press "add" 
3.Use the "Type" drop down to filter available NinjaScript types  
4.Select all of the files that you want to export and press the "OK" button 
5.A list of all files that will be exported will be shown 
6.Press the "Export" button to export the selected files 
7.A file dialog will open where you can choose the location your zip export file will be created in. Per default the NinjaScript Archive File (.zip) file will be created in My Documents\<ninjatrader folder="">\bin\Custom\ExportNinjaScript. 
8.The file can be [imported](import.htm) by another NinjaTrader application on a different PC  
 
  | ExportNinjaScript_1 | ExportNinjaScript_2 |
|   |



![tog_minus](tog_minus.gif)        [Exporting NinjaScript as Assembly](javascript:HMToggle('toggle','ExportingninjascriptAsAssembly','ExportingninjascriptAsAssembly_ICON'))




|  |  |
| --- | --- |
| You may want to provide other NinjaTrader users with access to your proprietary indicators or strategies in a secure format preventing them from being able to see your proprietary source code. You can do this by exporting your NinjaScript indicators as a compiled Microsoft .NET assembly (DLL) file. 
 
•This is a great distribution option if your proprietary indicator or strategy files do not reference external DLL's •If your proprietary indicator or strategy references external DLL's then its advised to create your own custom installer  
1.From the Control Center window select the menu Tools &gt; Export &gt; NinjaScript... to open the "Export NinjaScript" dialog window 2.Select the option "Export as compiled assembly".3.You can optionally select "Protect compiled assembly" (For information on protection see the "[Protection/DLL Security](protection_dll_security.htm) page) 4.Press "add"5.Use the "Type" drop down to filter available NinjaScript types6.Select all of the files that you want to export and press the "OK" button7.A list of all files that will be exported will be shown8.Optionally enter information that describes the assembly in the "Product" and "Version" fields9.Press the "Export" button to export the selected files 10.A file dialog will open where you can choose the location your zip export file will be created in. Per default the NinjaScript Archive File (.zip) file will be created in My Documents\<ninjatrader folder="">\bin\Custom\ExportNinjaScript.11.The file can be imported by another NinjaTrader application on a different PC 
  | ExportNinjaScript_3 |
|   |






 
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
 
 
 


HMInitToggle('ExportingninjascriptAsSourceFiles\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'ExportingninjascriptAsSourceFiles\',\'ExportingninjascriptAsSourceFiles\_ICON\')');
HMInitToggle('ExportingninjascriptAsSourceFiles','hm.type','dropdown','hm.state','0');
HMInitToggle('ExportingninjascriptAsAssembly\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'ExportingninjascriptAsAssembly\',\'ExportingninjascriptAsAssembly\_ICON\')');
HMInitToggle('ExportingninjascriptAsAssembly','hm.type','dropdown','hm.state','0');



</ninjatrader></ninjatrader>