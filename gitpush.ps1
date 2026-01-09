# Quick Git Commit and Push Script
# Usage: .\gitpush.ps1 "Your commit message"
# Example: .\gitpush.ps1 "Update RAG filtering logic"

param(
    [Parameter(Mandatory=$true)]
    [string]$CommitMessage
)

Write-Host "🔄 Adding all changes..." -ForegroundColor Cyan
git add -A

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git add failed!" -ForegroundColor Red
    exit 1
}

Write-Host "📝 Committing: $CommitMessage" -ForegroundColor Cyan
git commit -m "$CommitMessage"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git commit failed!" -ForegroundColor Red
    exit 1
}

Write-Host "🚀 Pushing to origin main..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git push failed!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Successfully pushed!" -ForegroundColor Green
Write-Host "🌐 Render will auto-deploy in ~2 minutes" -ForegroundColor Yellow
