param(
    [Parameter(Position = 0)]
    [ValidateSet('help','setup','debug','seed','run','test','snapshot','docs','clean','all')]
    [string]$Task = 'help'
)

$ErrorActionPreference = 'Stop'

function Invoke-Step {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Command
    )

    Write-Host "> $Command" -ForegroundColor Cyan
    Invoke-Expression $Command
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code $LASTEXITCODE: $Command"
    }
}

function Show-Help {
    Write-Host "dbt-task.ps1 - Makefile-like task runner for this project"
    Write-Host ""
    Write-Host "Usage:"
    Write-Host "  ./dbt-task.ps1 <task>"
    Write-Host ""
    Write-Host "Tasks:"
    Write-Host "  help      Show this help"
    Write-Host "  setup     Install/upgrade dbt dependencies in .venv"
    Write-Host "  debug     Validate dbt connection/profile"
    Write-Host "  seed      Load seed data"
    Write-Host "  run       Run models"
    Write-Host "  test      Run tests"
    Write-Host "  snapshot  Run snapshots"
    Write-Host "  docs      Generate docs"
    Write-Host "  clean     Clean dbt artifacts"
    Write-Host "  all       seed + run + test + snapshot"
}

switch ($Task) {
    'help' {
        Show-Help
    }
    'setup' {
        if (-not (Test-Path '.venv')) {
            Invoke-Step "python -m venv .venv"
        }
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; python -m pip install --upgrade pip"
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; pip install dbt-core dbt-databricks"
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt --version"
    }
    'debug' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt debug"
    }
    'seed' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt seed"
    }
    'run' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt run"
    }
    'test' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt test"
    }
    'snapshot' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt snapshot"
    }
    'docs' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt docs generate"
    }
    'clean' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt clean"
    }
    'all' {
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt seed"
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt run"
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt test"
        Invoke-Step ". ./.venv/Scripts/Activate.ps1; dbt snapshot"
    }
}
