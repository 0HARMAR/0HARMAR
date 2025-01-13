for ($i = 32; $i -le 126; $i++) {
    $char = [char]$i
    $hex = '{0:X}' -f $i
    Write-Host (" {0,3} | {1,3} | {2,4}" -f $i, $hex, $char)
}