if ($args[0] -eq "start") {
  pktmon start -c --comp 14 -m real-time
}
elseif ($args[0] -eq "etl2txt") {
  pktmon etl2txt C:\Windows\system32\PktMon.etl
}
elseif ($args[0] -eq "list") {
  pktmon list
}
else {
  Write-Host "Invalid argument."
}
