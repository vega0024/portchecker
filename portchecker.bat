@echo off
set /p target_ip="Enter target IP address: "
set /p port="Enter port number: "

echo Testing connection to %target_ip%:%port%...v24

:loop
timeout /t 1 >nul
for /f "tokens=1-3 delims=:" %%a in ("%TIME%") do (
    set "timestamp=%%a:%%b:%%c"
)
powershell.exe -Command "$socket = New-Object System.Net.Sockets.TcpClient; $result = $socket.BeginConnect('%target_ip%', %port%, $null, $null); $timeout = $result.AsyncWaitHandle.WaitOne(2000, $false); if ($timeout -and $socket.Connected) { Write-Host '%timestamp% - The port %port% is open on %target_ip%.' -ForegroundColor Green; $socket.Close() } else { Write-Host '%timestamp% - The port %port% is closed on %target_ip%.' -ForegroundColor Red; $socket.Close() }; exit"

goto loop
