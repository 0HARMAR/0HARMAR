查看pci
Get-WmiObject -Class Win32_PnPEntity | Where-Object { $_.DeviceID -like 'PCI*' } | Format-Table -Property Name, DeviceID, Status

查看usb
Get-WmiObject -Class Win32_PnPEntity | Where-Object { $_.DeviceID -like 'USB*' } | Format-Table -Property Name, DeviceID, Status
