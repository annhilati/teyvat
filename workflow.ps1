$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$envFile = Join-Path $scriptDir ".env"
$beetStdoutLog = Join-Path $scriptDir "beet-watch.stdout.log"
$beetStderrLog = Join-Path $scriptDir "beet-watch.stderr.log"

function Import-EnvFile {
    param([string]$Path)

    if (-not (Test-Path $Path)) {
        return
    }

    foreach ($line in Get-Content $Path) {
        $trimmed = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed) -or $trimmed.StartsWith("#")) {
            continue
        }

        $parts = $trimmed -split "=", 2
        if ($parts.Count -eq 2) {
            $name = $parts[0].Trim()
            $value = $parts[1].Trim().Trim('"').Trim("'")
            [System.Environment]::SetEnvironmentVariable($name, $value, "Process")
        }
    }
}

function Stop-ManagedProcess {
    param([System.Diagnostics.Process]$Process)

    if ($Process -and -not $Process.HasExited) {
        try {
            Stop-Process -Id $Process.Id -Force -ErrorAction SilentlyContinue
            $Process.WaitForExit(5000) | Out-Null
        }
        catch {
        }
    }
}

function Stop-PortListener {
    param([int]$Port)

    try {
        $listeners = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
        foreach ($listener in $listeners) {
            $process = Get-Process -Id $listener.OwningProcess -ErrorAction SilentlyContinue
            if ($process) {
                Write-Host "Beende bestehenden Listener auf Port $Port (PID $($process.Id))..."
                Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
            }
        }
    }
    catch {
    }
}

Import-EnvFile -Path $envFile

if ([string]::IsNullOrWhiteSpace($env:WORLD_PATH)) {
    throw "Bitte setze WORLD_PATH in .env"
}

Stop-PortListener -Port 8000

$beetProcess = $null

try {
    Write-Host "Starte beet watch..."
    $beetProcess = Start-Process -FilePath "beet" -ArgumentList @("watch", "-l", $env:WORLD_PATH, "--config", (Join-Path $scriptDir "beet.yml")) -WorkingDirectory $scriptDir -RedirectStandardOutput $beetStdoutLog -RedirectStandardError $beetStderrLog -PassThru

    Write-Host "Starte rhombus preview..."
    Push-Location $scriptDir
    try {
        & rhombus preview "Teyvat"
    }
    finally {
        Pop-Location
    }
}
finally {
    Stop-ManagedProcess -Process $beetProcess
}

